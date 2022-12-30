#Print all possible subsets
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
    
    opReject = opReject + ip[0]
    opInclude = opInclude + ip[0].upper()

    ip = ip[1:]
    printSubsets(ip, opReject)
    printSubsets(ip, opInclude)
#Driver code
ip = "ab"
op = ""
res = []
printSubsets(ip,op)
print("Result: ",res)