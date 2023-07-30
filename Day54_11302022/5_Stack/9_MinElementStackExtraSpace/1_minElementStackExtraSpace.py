#Function
def push(a):
    stack.append(a)
    if(len(ss) == 0 or a<=ss[-1]):
        ss.append(a)# Imp to store the repeated element to avoid issues while pop() and for that = sign is used
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
ss = [] #Extra Space; used to store the min element

minEleExtraSpace(arr, n)