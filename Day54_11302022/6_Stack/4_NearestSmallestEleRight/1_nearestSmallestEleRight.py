#Next Greatest Element to Right for every array
#Function
def nearestSmallestElementToRight(arr, n):
    for i in range(n-1,-1,-1):
        if(len(stack) == 0):
            res.append(-1)
        elif(len(stack)>0 and stack[-1]<arr[i]):
            res.append(stack[-1])
        elif(len(stack) > 0 and stack[-1] >= arr[i]):
            print(arr[i])
            while(len(stack) > 0 and stack[-1]>=arr[i]):
                flag = 0
                if(len(stack)==1 and stack[-1] == arr[i]):
                    res.append(stack[-1])
                    stack.pop()
                    flag = 1
                    break
                stack.pop()
            if(flag!=1):
                if(len(stack) == 0):
                    res.append(-1)
                else:
                    res.append(stack[-1])
        
        stack.append(arr[i])

        

#Driver Code
stack = []
res = []
arr = [2,3,3,1]
n = len(arr)
print("Nearest Smallest element to right: ")
nearestSmallestElementToRight(arr, n)
print(arr)
res.reverse()
print(res)