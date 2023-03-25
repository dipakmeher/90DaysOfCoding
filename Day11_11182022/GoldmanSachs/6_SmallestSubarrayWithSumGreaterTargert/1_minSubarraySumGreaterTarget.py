#Function
def largestSubarrayofSumK(arr,n,Sum):
    i = 0
    j = 0
    subsum = 0
    mx = n+1
    count = 0
    while(j<n):
        subsum = subsum + arr[j]
        print("arr[j]",arr[j])
        print("Subsum: ", subsum)
        
        if(subsum < Sum):
            j+=1
        # elif(subsum == Sum):
        #     mx = max(mx, j-i+1)
        #     count+=1
        #     j+=1
        elif(subsum > Sum):
            mx = min(mx, j-i+1)
            while(subsum >=Sum):
                subsum = subsum - arr[i]
                print("arr[i]",arr[i])
                print("subsum after delete: ",subsum)
                i+=1 
            j+=1
        print()
                
    print("Smallest subarray of sum k is of size",mx)

#Driver Code
# arr = [4,1,1,2,1,1,5]
arr = [1,2,3,6,5,7]
n = len(arr)
Sum = 11
largestSubarrayofSumK(arr,n,Sum)