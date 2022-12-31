# generate the paranthesis 
#Function
def generateBalancedParen(open,closed, op):
    global res
    if(open == 0 and closed == 0):
        res.append(op)
        return
    op1 = op # Learning: Don't miss initializing this outputs with op
    op2 = op # Learning: Don't miss initializing this outputs with op
    if(open != 0): 
        print("open: ", open)
        op1 = op1 + "("
        # open = open-1
        generateBalancedParen(open-1,closed,op1)
   
    if(open<closed): # we are allowed to add more open brackets
        print("Open: ", open)
        op2 = op2 + ")"
        # closed = closed - 1
        generateBalancedParen(open,closed - 1,op2)
     
    
#Driver Code
n = 3
c = n #closed brackets
o = n #open brackets
op1=""
res = []
generateBalancedParen(o,c, op1)
print(res)