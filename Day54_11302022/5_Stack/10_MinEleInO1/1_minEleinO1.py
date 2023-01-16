
#Functions
def push(a):
    global minEle

    if(len(stack) == 0):
        stack.append(a)
        minEle = a
    else:
        if(a>=minEle):
            stack.append(a)
        elif(a<minEle):
            stack.append(2*a - minEle)
            minEle = a

def pop():
    global minEle
    if(len(stack) == 0):
        return -1
    else:
        if(stack[-1] >= minEle):
            return stack.pop()
        elif(stack[-1]<minEle):
            minEle = 2 * minEle - stack[-1]
            return stack.pop()

def top():
    global minEle
    if(len(stack) == 0):
        return -1
    else:
        if(stack[-1] >= minEle):
            return stack[-1]
        elif(stack[-1]<minEle):
            return minEle
        
def minEleOOfOne(arr,n):
    for i in arr:
        push(i)
    print("stack: ",stack)
    print("Pop: ", pop())
    print("Top: ", top())
    print("Min element in stack: ",minEle)

#Driver Code
arr = [18,19,2,15,15]
stack = []
n = len(stack)
ss = []
minEle = -1

minEleOOfOne(arr, n)