# Reverse a stack using recursion
from collections import deque
# Function
def stackReverse(stack):
    if(len(stack) == 1):
        return
    
    temp = stack.pop()
    stackReverse(stack)
    stack.insert(0,temp)
# Driver Code
stack = deque(['1','2','5','4','3'])
print("stack before reverse: ", stack)
stackReverse(stack)
print("stack after reverse: ", stack)