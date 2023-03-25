#Function
def rainTrapping(arr, n):
    l = 0
    r = n-1
    lmax = arr[0]
    rmax = arr[n-1]
    water = 0
    while(l<=r):
        if(arr[l]<=arr[r]):
            if(arr[l]>lmax):
                lmax = arr[l]
            else:
                water+=(lmax-arr[l])
            l+=1
        else:
            if(arr[r]>rmax):
                rmax = arr[r]
            else:
                water+=(rmax-arr[r])
            r-=1

    return water

#Driver Code
arr = [3,0,0,2,0,4]
n = len(arr)
print(arr)
print("Total rain water trapped in these building is ",rainTrapping(arr,n))