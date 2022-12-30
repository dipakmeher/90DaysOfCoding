#Print all possible subsets
#function
def printSubsets(ip, op):
    global count
    if(len(ip) == 0):
        count = count + 1
        print("Subset count: ",count)
        print(op)
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
s1 = "ab"
ip = "aab"
op=""
count = 0
printSubsets(ip,op)