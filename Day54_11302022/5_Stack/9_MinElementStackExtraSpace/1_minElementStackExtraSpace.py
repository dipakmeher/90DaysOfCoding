#Function
def push(a):
    stack.append(a)
    if(len(ss) == 0 or a<=ss[-1]):
        ss.append(a)
    return
def pop():
    if(len(stack) == 0):
        return -1
    ans = stack.pop()
    if(ss[-1] == ans):
        ss.pop()
    
def getMin():
    if(len(ss) == 0):
        return -1
    return ss[-1]

def minEleExtraSpace(arr, n):
    for i in arr:
        push(i)

    pop()
    print("Min element in stack: ",getMin())

#Driver Code
arr = [18,19,25,15,15]
stack = []
n = len(stack)
ss = []

minEleExtraSpace(arr, n)