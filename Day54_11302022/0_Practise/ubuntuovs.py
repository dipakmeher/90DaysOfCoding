"""
OpenNSA Ubuntu Backend

Authors: 

"""

import random

from twisted.python import log
from twisted.internet import defer

from opennsa import constants as cnt, config
from opennsa.backends.common import ssh, genericbackend

LOG_SYSTEM = 'opennsa.ubuntubackend'
# parameterized commands
COMMAND_ECHO            = 'echo'

import random
import string

created_bridges = []

def generate_bridge_name():
    bridge_name = f"bridge{''.join(random.choices(string.ascii_lowercase, k=6))}"
    while bridge_name in created_bridges:
        bridge_name = f"bridge{''.join(random.choices(string.ascii_lowercase, k=6))}"
    created_bridges.append(bridge_name)
    return bridge_name

configurations = {}  # Dictionary to store configurations


def createConfigureCommands(segment_id, source_nrm_port, dest_nrm_port, source_vlan, dest_vlan):
    bridge_name = generate_bridge_name()

    commands = []

    # Create the bridge
    bridge_command = f"sudo ip link add name {bridge_name} type bridge"
    commands.append(bridge_command)

    # Add VLAN to source port and attach to the bridge
    source_vlan_command = f"sudo ip link add link {source_nrm_port} name {source_nrm_port}.{source_vlan} type vlan id {source_vlan}"
    source_vlan_up_command = f"sudo ip link set {source_nrm_port}.{source_vlan} up"
    source_vlan_attach_command = f"sudo ip link set {source_nrm_port}.{source_vlan} master {bridge_name}"
    commands.extend([source_vlan_command, source_vlan_up_command, source_vlan_attach_command])

    # Add VLAN to destination port and attach to the bridge
    dest_vlan_command = f"sudo ip link add link {dest_nrm_port} name {dest_nrm_port}.{dest_vlan} type vlan id {dest_vlan}"
    dest_vlan_up_command = f"sudo ip link set {dest_nrm_port}.{dest_vlan} up"
    dest_vlan_attach_command = f"sudo ip link set {dest_nrm_port}.{dest_vlan} master {bridge_name}"
    commands.extend([dest_vlan_command, dest_vlan_up_command, dest_vlan_attach_command])

    # Store the configuration in the dictionary
    configurations[segment_id] = (source_nrm_port, source_vlan, dest_nrm_port, dest_vlan, bridge_name)

    return commands


def createDeleteCommands(unique_id):
    if unique_id in configurations:
        source_nrm_port, source_vlan, dest_nrm_port, dest_vlan, bridge_name = configurations[unique_id]

        commands = []

        # Delete the VLAN interfaces and detach from the bridge
        source_vlan_detach_command = f"sudo ip link set {source_nrm_port}.{source_vlan} nomaster"
        source_vlan_delete_command = f"sudo ip link delete {source_nrm_port}.{source_vlan}"
        dest_vlan_detach_command = f"sudo ip link set {dest_nrm_port}.{dest_vlan} nomaster"
        dest_vlan_delete_command = f"sudo ip link delete {dest_nrm_port}.{dest_vlan}"
        commands.extend([source_vlan_detach_command, source_vlan_delete_command, dest_vlan_detach_command, dest_vlan_delete_command])

        # Delete the bridge
        bridge_delete_command = f"sudo ip link delete {bridge_name}"
        commands.append(bridge_delete_command)

        # Remove the configuration from the dictionary and created_bridges list
        del configurations[unique_id]
        created_bridges.remove(bridge_name)

        return commands
    else:
        return ["Configuration with given ID not found."]


class SSHChannel(ssh.SSHChannel):

    name = 'session'

    def __init__(self, conn):
        ssh.SSHChannel.__init__(self, conn=conn)

        self.data = ''

        self.wait_defer = None
        self.wait_data  = None


    @defer.inlineCallbacks
    def sendCommands(self, commands):
        LT = '\n' # line termination

        try:
            yield self.conn.sendRequest(self, 'shell', '', wantReply=1)

#            time.sleep(1) # FIXME
            d = self.waitForData('\n')
            self.write(COMMAND_ECHO + LT)
            yield d

            log.msg('Ready', debug=True, system=LOG_SYSTEM)

            for cmd in commands:
                log.msg('CMD> %s' % cmd, system=LOG_SYSTEM)
                d = self.waitForData('\n')
                self.write(cmd + LT)
                self.write(COMMAND_ECHO + LT)
#                time.sleep(1) # FIXME
                yield d

            # commit commands, check for 'commit complete' as success
            # not quite sure how to handle failure here

            ## test stuff
            #d = self.waitForData('[edit]')
            #self.write('commit check' + LT)

            #d = self.waitForData('commit complete')
            #self.write(COMMAND_COMMIT + LT)
            #yield d

        except Exception as e:
            log.msg('Error sending commands: %s' % str(e))
            raise e

        d = self.waitForData('\n')
        self.write(COMMAND_ECHO + LT)
        yield d
        log.msg('Commands successfully sent', system=LOG_SYSTEM)
        self.sendEOF()
        self.closeIt()


    def waitForData(self, data):
        self.wait_data  = data
        self.wait_defer = defer.Deferred()
        return self.wait_defer


    def dataReceived(self, data):
        if len(data) == 0:
            pass
        else:
            self.data += data
            if self.wait_data and self.wait_data in self.data:
                d = self.wait_defer
                self.data       = ''
                self.wait_data  = None
                self.wait_defer = None
                d.callback(self)


class UbuntuCommandSender:


    def __init__(self, host, port, ssh_host_fingerprint, user, ssh_public_key_path, ssh_private_key_path, db_ip):

        self.ssh_connection_creator = \
             ssh.SSHConnectionCreator(host, port, [ ssh_host_fingerprint ], user, ssh_public_key_path, ssh_private_key_path)
        self.db_ip = db_ip

        log.msg('SSH connection arguments %s, %s, %s, %s, %s, %s' % (host, port, ssh_host_fingerprint, user, ssh_public_key_path, ssh_private_key_path), system=LOG_SYSTEM)


    @defer.inlineCallbacks
    def _sendCommands(self, commands):

        log.msg('Creating new SSH connection', system=LOG_SYSTEM)

        ssh_connection = yield self.ssh_connection_creator.getSSHConnection()

        try:
            ssh_channel = SSHChannel(conn = ssh_connection)
            ssh_connection.openChannel(ssh_channel)
            yield ssh_channel.channel_open
            yield ssh_channel.sendCommands(commands)
            # not a yield, just being nice
            ssh_channel.loseConnection()

        finally:
            # twisted/os will flush data, before closing
            ssh_connection.transport.loseConnection()


    def setupLink(self, source_target, dest_target):
        seg_id = len(configurations) + 1  # Unique ID counter

        commands = createConfigureCommands(seg_id, source_target.port, dest_target.port, source_target.vlan, dest_target.vlan)
        return self._sendCommands(commands)


    def teardownLink(self, source_target, dest_target):

        # commands = createDeleteCommands(self.db_ip, source_target.port, dest_target.port, source_target.vlan, dest_target.vlan)
        commands = createDeleteCommands(self.db_ip, source_target.port, dest_target.port, source_target.vlan, dest_target.vlan)
        return self._sendCommands(commands)


# --------


class UbuntuTarget(object):

    def __init__(self, port, vlan=None):
        self.port = port
        self.vlan = vlan

    def __str__(self):
        if self.vlan:
            return '<UbuntuTarget %s#%i>' % (self.port, self.vlan)
        else:
            return '<UbuntuTarget %s>' % self.port



class UbuntuConnectionManager:

    def __init__(self, port_map, host, port, host_fingerprint, user, ssh_public_key, ssh_private_key, db_ip):

        self.port_map = port_map
        self.command_sender = UbuntuCommandSender(host, port, host_fingerprint, user, ssh_public_key, ssh_private_key, db_ip)


    def getResource(self, port, label):
        assert label is not None or label.type_ == cnt.ETHERNET_VLAN, 'Label type must be VLAN'
        # resource is port + vlan (router / virtual switching)
        label_value = '' if label is None else label.labelValue()
        return port + ':' + label_value


    def getTarget(self, port, label):
        assert label is not None and label.type_ == cnt.ETHERNET_VLAN, 'Label type must be VLAN'
        vlan = int(label.labelValue())
        assert 1 <= vlan <= 4095, 'Invalid label value for vlan: %s' % label.labelValue()

        return UbuntuTarget(self.port_map[port], vlan)


    def createConnectionId(self, source_target, dest_target):
        return 'UbuntuBackend-' + str(random.randint(100000,999999))


    def canSwapLabel(self, label_type):
        return True


    def setupLink(self, connection_id, source_target, dest_target, bandwidth):

        def linkUp(_):
            log.msg('Link %s -> %s up' % (source_target, dest_target), system=LOG_SYSTEM)

        d = self.command_sender.setupLink(source_target, dest_target)
        d.addCallback(linkUp)
        return d


    def teardownLink(self, connection_id, source_target, dest_target, bandwidth):

        def linkDown(_):
            log.msg('Link %s -> %s down' % (source_target, dest_target), system=LOG_SYSTEM)

        d = self.command_sender.teardownLink(source_target, dest_target)
        d.addCallback(linkDown)
        return d



def UbuntuBackend(network_name, nrm_ports, parent_requester, cfg):

    name = 'UbuntuBackend %s' % network_name
    nrm_map  = dict( [ (p.name, p) for p in nrm_ports ] ) # for the generic backend
    port_map = dict( [ (p.name, p.interface) for p in nrm_ports ] ) # for the nrm backend

    # ================================================================
    # Need to change the below items
    # ================================================================

    # extract config items
    host             = cfg[config.PICA8OVS_HOST]
    port             = cfg.get(config.PICA8OVS_PORT, 22)
    host_fingerprint = cfg[config.PICA8OVS_HOST_FINGERPRINT]
    user             = cfg[config.PICA8OVS_USER]
    ssh_public_key   = cfg[config.PICA8OVS_SSH_PUBLIC_KEY]
    ssh_private_key  = cfg[config.PICA8OVS_SSH_PRIVATE_KEY]
    db_ip            = cfg[config.PICA8OVS_DB_IP]

    cm = UbuntuConnectionManager(port_map, host, port, host_fingerprint, user, ssh_public_key, ssh_private_key, db_ip)
    return genericbackend.GenericBackend(network_name, nrm_map, cm, parent_requester, name)

