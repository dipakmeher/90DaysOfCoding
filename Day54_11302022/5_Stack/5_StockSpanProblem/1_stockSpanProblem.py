#StockSpan Problem
#Function
#Update 02152023##############
# We have made use of stack here because we have to traverse through array 
# from current element to start order to check the condition and 
# that too for each element
# So it would be easier to use stack that gives us the previous element 
# using stack.top()

def nearestGretestElementToLeft(arr, n):
    for i in range(0,n):
        if(len(stack) == 0):
            res.append(-1)
        elif(len(stack)>0 and stack[-1][0]>arr[i]):
            res.append(stack[-1][1])
        elif(len(stack) > 0 and stack[-1][0] <= arr[i]):
            while(len(stack) > 0 and stack[-1][0]<=arr[i]):
                stack.pop()
            if(len(stack) == 0):
                res.append(-1)
            else:
                res.append(stack[-1][1])
        stack.append([arr[i],i])

        

#Driver Code
stack = []
res = []
arr = [1,3,2,4]
n = len(arr)
print("Nearest Greatest element to left: ")
nearestGretestElementToLeft(arr, n)
print("res before modification: ",res)
for i in range(n):
    res[i] = i - res[i]
print(arr)
print(res)