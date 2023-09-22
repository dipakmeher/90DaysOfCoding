#Function
#Rev
def largestSubarrayofSumK(arr,n,Sum):
    i = 0
    j = 0
    subsum = 0
    mx = 0
    count = 0
    while(j<n):
        subsum = subsum + arr[j]
        print("arr[j]",arr[j])
        print("Subsum: ", subsum)
        
        if(subsum < Sum):
            j+=1
        elif(subsum == Sum):
            mx = max(mx, j-i+1)
            count+=1
            j+=1
        elif(subsum > Sum):
            while(subsum > Sum):
                subsum = subsum - arr[i]
                print("arr[i]",arr[i])
                print("subsum after delete: ",subsum)
                i+=1 
            j+=1
        print()
                
    print("largest subarray of sum k is of size",mx)
    print("count",count)

#Driver Code
arr = [4,1,1,2,1,1,5]
n = len(arr)
Sum = 5
largestSubarrayofSumK(arr,n,Sum)