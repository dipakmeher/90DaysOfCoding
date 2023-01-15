#Function
def rainTrapping(arr, n):
    maxFromLeft = [0]*n
    maxFromRight = [0]*n

    maxFromLeft[0] = arr[0]
    for i in range(1,n):
        maxFromLeft[i] = max(maxFromLeft[i-1],arr[i])
    
    print(maxFromLeft)
    mr = arr[n-1]
    for j in range(n-1,-1,-1):
        maxFromRight[j] = max(mr,arr[j])
    print(maxFromRight)
    water = [0]*n
    for i in range(n):
        water[i] = min(maxFromLeft[i], maxFromRight[i]) - arr[i]

    print(water)
    sum = 0
    for i in range(n):
        sum  = sum + water[i]

    return sum

#Driver Code
arr = [3,0,0,2,0,4]
n = len(arr)
print(arr)
print("Total rain water trapped in these building is ",rainTrapping(arr,n))