# Right answer
def beautyOfArray(arr, c, n, i):
    if(len(arr) == i or i == n):
        return c
    if(arr[i] == i+1):
        ans = c+1
        return beautyOfArray(arr, ans, n, i+1)
    else:
        arr2 = arr[:]
        arr2.pop(i)
        ans1 = max(beautyOfArray(arr, c, n,i+1), beautyOfArray(arr2,c,len(arr2),i))
        return ans1
    

# arr = [1,3,2,5,4,5,3]
arr = [1,3,2,5,4,5,3]
c = 0
n = len(arr)
print("Arr",arr)
print("Count of Bounty: ", beautyOfArray(arr,c,n, 0))