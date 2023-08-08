#need to solve tomorrow
def beautyOfArray(arr, c, n):
    if(len(arr) == 0 or n == 0):
        return c 

    #include
    if(arr[n-1] == n-1):
        c+=1
    res = max(beautyOfArray(arr, c, n-1),beautyOfArray(arr[:n], c, n-1))
    print("Result: ",res)
    

arr = [1,3,2,5,4,5,3]
c = 0
n = len(arr)
print(beautyOfArray(arr,c,n))