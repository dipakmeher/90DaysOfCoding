#Next Greatest Element for every element in array 
#Function
def nearestGretestElementToRight(arr, n):
    for i in range(n-1,-1,-1):
        if(len(stack) == 0):
            res.append(-1)
        elif(len(stack)>0 and stack[-1]>arr[i]):
            res.append(stack[-1])
        elif(len(stack) > 0 and stack[-1] <= arr[i]):
            while(len(stack) > 0 and stack[-1]<=arr[i]):
                stack.pop()
            if(len(stack) == 0):
                res.append(-1)
            else:
                res.append(stack[-1])
        stack.append(arr[i])

        

#Driver Code
stack = []
res = []
arr = [1,3,2,4]
n = len(arr)
nearestGretestElementToRight(arr, n)
print(arr)
res.reverse()
print(res)