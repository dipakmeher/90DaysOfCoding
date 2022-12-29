#Delete middle element of a stack
from collections import deque
#function
def DeleteMiddleElement(stack,deleteEle):
    #BC
    if(deleteEle == 1):
        stack.pop()
        return
    #HP
    # temp = stack[len(stack)-1]
    temp = stack.pop()
    DeleteMiddleElement(stack,deleteEle-1)
    #ID
    stack.append(temp)
    return stack

#driver code
stack = deque(['1','2','5','3','4'])
print("Stack before deletion: ", stack)
deleteEle = len(stack)//2 + 1
print(deleteEle)
DeleteMiddleElement(stack,deleteEle)
print("Stack after deletion: ", stack)