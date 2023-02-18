#MaxAreaOfHistagram 
#Function
def nearestSmallestElementToRight(arr, n):
    stack = []
    res = []
    for i in range(n-1,-1,-1):
        if(len(stack) == 0):
            res.append(n) # Modification in code
        elif(len(stack)>0 and stack[-1][0]<arr[i]):
            res.append(stack[-1][1])
        elif(len(stack) > 0 and stack[-1][0]>= arr[i]):
            while(len(stack) > 0 and stack[-1][0]>=arr[i]):
                stack.pop()
            if(len(stack) == 0):
                res.append(n) #Modification in NSR code
            else:
                res.append(stack[-1][1]) 
        stack.append([arr[i],i])
    res.reverse()
    return res

def nearestSmallestElementToLeft(arr, n):
    stack = []
    res = []
    for i in range(0,n):
        if(len(stack) == 0):
            res.append(-1)
        elif(len(stack)>0 and stack[-1][0]<arr[i]):
            res.append(stack[-1][1])
        elif(len(stack) > 0 and stack[-1][0] >= arr[i]):
            while(len(stack) > 0 and stack[-1][0]>=arr[i]):
                stack.pop()
            if(len(stack) == 0):
                res.append(-1)
            else:
                res.append(stack[-1][1])
        stack.append([arr[i],i])
    return res
    
#Driver Code
# arr = [6,2,5,4,5,1,6]
arr = [2,3,3,2]
n = len(arr)
nsr = nearestSmallestElementToRight(arr, n)
nsl = nearestSmallestElementToLeft(arr, n)
print(arr)
print("nsr", nsr)
print("nsl", nsl)
print("Max Area of Histogram ")

maxArea = -1
for i in range(n):
    width = nsr[i] - nsl[i] - 1
    Area = arr[i] * width
    maxArea = max(maxArea, Area)

print(maxArea)