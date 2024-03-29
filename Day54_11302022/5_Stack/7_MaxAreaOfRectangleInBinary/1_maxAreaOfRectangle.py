# Max area of Histogram
def nearestSmallestElementToRight(arr, n):
    stack = []
    res = []
    for i in range(n-1,-1,-1):
        if(len(stack) == 0):
            res.append(n)
        elif(len(stack)>0 and stack[-1][0]<arr[i]):
            res.append(stack[-1][1])
        elif(len(stack) > 0 and stack[-1][0]>= arr[i]):
            while(len(stack) > 0 and stack[-1][0]>=arr[i]):
                stack.pop()
            if(len(stack) == 0):
                res.append(-1)
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

def MaxAreaHistogram(arr):
    n = len(arr)
    nsr = nearestSmallestElementToRight(arr, n)
    nsl = nearestSmallestElementToLeft(arr, n)

    tempMax = -1
    for i in range(n):
        width = nsr[i] - nsl[i] - 1
        Area = arr[i] * width
        tempMax = max(tempMax, Area)
    return tempMax

#Driver Code
arr = [
    [0,1,1,0],
    [1,1,1,1],
    [1,1,1,1],
    [1,1,0,0]
]
n = len(arr)
m = len(arr[0])
res = []
for i in range(m):
    res.append(arr[0][i])

maxArea = MaxAreaHistogram(res)
for i in range(1,n):
    for j in range(m):
        if(arr[i][j] == 0):
            res[j] = 0
        else:
            res[j] = res[j] + arr[i][j]
    tempArea = MaxAreaHistogram(res)
    maxArea = max(maxArea, tempArea)
    

print("Max Area of Reactangle: ", maxArea)
