# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.

#Brute Foce -  Cheking for each varied window size
# TC: N2

def maxSubarray(nums,n):
    mx = -1000
    # 
    ans = []
    for sub_array in range(1,n+1):
        res = list()
        teString = ""
        sum = 0
        for start_index in range(0,n):
            if(sub_array+start_index > n):
                break
            sum = sum + nums[sub_array+start_index - 1]
            res.append(nums[sub_array+start_index - 1])
            if(sum>mx): 
                mx = sum
                ans = []
                ans.append(res[:])
        print()
    return mx,ans[-1]
nums = [-2,1,-3,4,-1,2,1,-5,4]
n = len(nums)
print(maxSubarray(nums,n))