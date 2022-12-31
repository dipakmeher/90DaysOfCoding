#Letter Case Permutations: Recursions
#function
def printSubsets(ip, op):
    global count
    if(len(ip) == 0):
        res.append(op)
        return
    
    #Equating list is like a pointing to the address of the list through new variable
    # and would refer to the same original list. Any changes made into new one will relect into old one
    opReject = op # reject
    opInclude = op #include #imp step as we have to append the output with previous one
    
    # if(ip[0].isalpha()):
    if(ip[0].isupper()):
        opInclude = opInclude + ip[0].lower()
        opInclude = opInclude + ip[1]
    else:
        opInclude = opInclude + ip[0].upper()
        opInclude = opInclude + ip[1]
    opReject = opReject + ip[0]
    opReject = opReject + ip[1]
    # else:
    #     opInclude = opInclude + ip[0]
    #     opReject = opReject + ip[0]

    ip = ip[2:]
    printSubsets(ip, opReject)
    printSubsets(ip, opInclude)
#Driver code
ip = "a1B2"
op = ""
res = []
printSubsets(ip,op)
print("Result: ",res)