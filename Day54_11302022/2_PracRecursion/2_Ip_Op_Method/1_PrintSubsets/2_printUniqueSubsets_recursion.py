#Print all possible subsets
#function
def printSubsets(ip, op):
    if(len(ip) == 0):
        if op not in res:
            res.append(op)
        return
    
    #Equating list is like a pointing to the address of the list through new variable
    # and would refer to the same original list. Any changes made into new one will relect into old one
    opReject = op # reject
    opInclude = op #include #imp step as we have to append the output with previous one

    opInclude = opInclude + ip[0]
    ip = ip[1:]
    printSubsets(ip, opReject)
    printSubsets(ip, opInclude)
#Driver code
ip = "aab"
op=""
res=[]

printSubsets(ip,op)
print(res)