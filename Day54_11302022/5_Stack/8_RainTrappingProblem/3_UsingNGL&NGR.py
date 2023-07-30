#Not Possible; no need to use Stack since we don't have to store/remember last greatest element
#Function
def greatestElementToLeft(arr, n):
    stack = []
    res1 = []
    for i in range(0,n):# Only change in left and right code
        if(len(stack) == 0):
            res1.append(arr[i])
        elif(len(stack)>0 and stack[-1]>arr[i]):
            res1.append(stack[-1])
        elif(len(stack) > 0 and stack[-1] <= arr[i]):
            while(len(stack) > 0 and stack[-1]<=arr[i]):
                stack.pop()
            if(len(stack) == 0):
                res1.append(arr[i])
            else:
                res1.append(stack[-1])
        stack.append(arr[i])
    print("res1 = ",res1)
    return res1

def greatestElementToRight(arr, n):
    stack = []
    res2 = []
    for i in range(n-1,-1,-1):
        if(len(stack) == 0):
            res2.append(arr[i])
        elif(len(stack)>0 and stack[-1]>arr[i]):
            res2.append(stack[-1])
        elif(len(stack) > 0 and stack[-1] <= arr[i]):
            while(len(stack) > 0 and stack[-1]<=arr[i]):
                stack.pop()
            if(len(stack) == 0):
                res2.append(arr[i])
            else:
                res2.append(stack[-1])
        stack.append(arr[i])
    res2.reverse()
    print("res2 = ",res2)
    return res2


def rainTrapping(arr, n):
    # gl = [0]*n
    # gr = [0]*n
    gl = greatestElementToLeft(arr, n)
    gr = greatestElementToRight(arr,n)

    water = [0]*n
    for i in range(n):
        water[i] = min(gl[i], gr[i]) - arr[i]
    
    print(water)

#Driver Code
# stack = []
# res = []
arr = [3,2,0,2,4]
n = len(arr)
print("arr = ",arr)
print("Rain Trapping Problem: ")
rainTrapping(arr, n)
# greatestElementToLeft(arr, n)
# greatestElementToRight(arr,n)
# print(arr)
# print(res)