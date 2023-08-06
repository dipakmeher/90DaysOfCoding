#need to solve
def beautyOfArray(arr, c, n):
    if(len(arr) == 0):
        return c 

    #include
    if(arr[n] == n):
        c+=1
        beautyOfArray(arr, c, n-1)
        beautyOfArray(arr[:n], c, n)
    

arr = [1,3,2,5,4,5,3]
c = 0
n = len(arr)
beautyOfArray(arr,c,n)