# Wrong answer with the commented inputs, lets see
def beautyOfArray(arr, c, n):
    if(n == 0):
        return 0
    if(arr[n-1] == n):
        ans = 1+beautyOfArray(arr, c, n-1)
        return ans
    else:
        arr2 = arr[:]
        arr2.pop(n-1)
        ans1 = max(beautyOfArray(arr, c, n-1), beautyOfArray(arr2,c,len(arr2)))
        return ans1
    

# arr = [1,3,2,5,4,5,3]
arr = [1,3,2,5,4,5]
c = 0
n = len(arr)
print("Arr",arr)
print("Count of Bounty: ", beautyOfArray(arr,c,n))