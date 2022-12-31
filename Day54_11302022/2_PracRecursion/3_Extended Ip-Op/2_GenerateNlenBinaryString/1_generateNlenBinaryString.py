# generate the paranthesis: Here the condition is count(1)> count(0)
#Function
def generateNlenBinary(one,zero, n, op):
    global res
    if(n==0):
        res.append(op)
        return
    op1 = op # Learning: Don't miss initializing this outputs with op
    op2 = op # Learning: Don't miss initializing this outputs with op
    
    op1 = op1 + "1"
    generateNlenBinary(one-1,zero, n-1, op1)
    if(one<zero): # we are allowed to add more open brackets
        op2 = op2 + "0"
        # closed = closed - 1
        generateNlenBinary(one,zero - 1,n-1,op2)
     
    
#Driver Code
n = 3
one = n #closed brackets
zero = n #open brackets
op1=""
res = []
generateNlenBinary(one,zero, n, op1)
print(res) 