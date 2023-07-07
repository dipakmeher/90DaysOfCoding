#Delete middle element of a stack
from collections import deque
#function
def DeleteMiddleElement(stack,delindex):
    #BC
    if(delindex == 1):
        stack.pop()
        return
    #HP
    # temp = stack[len(stack)-1]
    temp = stack.pop()
    DeleteMiddleElement(stack,delindex-1)
    #ID
    stack.append(temp)
    return stack

#driver code
stack = deque(['1','2','5','3','4'])
print("Stack before deletion: ", stack)
delindex = len(stack)//2 + 1 #Index of element
print(stack[delindex])
DeleteMiddleElement(stack,delindex)
print("Stack after deletion: ", stack)