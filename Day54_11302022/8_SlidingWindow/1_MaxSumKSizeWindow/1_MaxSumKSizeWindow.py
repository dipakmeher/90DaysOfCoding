# Find the maximum sum subarray of window size k
# To continue tomorrow
#Function
def maxSumKSizeWindow(arr,n,k):
    i = 0
    j = 0
    Sum = 0
    mx = -1
    while(j<n):
        Sum = Sum + arr[j]
        print(Sum)
        if(j-i+1 < k): # j-i+1 is a window size
            j+=1
        elif(j-i+1 == k):
            mx = max(mx,Sum)
            Sum = Sum - arr[i]
            i+=1
            j+=1
    print("Max Sum Window of Size K is ", mx)

#Driver Code
arr = [ 100, 200, 300, 400]
n = len(arr)
k=2
print(arr)
maxSumKSizeWindow(arr,n,k)