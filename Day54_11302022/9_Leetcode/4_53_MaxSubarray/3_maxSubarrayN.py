# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.

# TC: N

def maxSubarray(nums,n):
    maxSum = -1000
    currSum = 0

    for i in range(n):
        currSum = max(currSum + nums[i] , nums[i])
        maxSum = max(maxSum, currSum)
    return maxSum

    # i = 0
    # j = 0
    # sum = 0
    # mx = nums[0]
    # flag = False
    # n = len(nums)
    # if(n == 1):
    #     return nums[n-1]
    # while(j<n):
    #     sum = sum + nums[j]
    #     # if(nums[j] >=0) :
    #     #     flag = True
    #     # if(flag == True):
    #     #     if(sum<0 and nums[j] <0):
    #     #         sum = 0
    #     #     else:
    #     #         sum = nums[j]
    #     #     i+=1
    #     # else:
    #     #     i+=1

    #     if(sum<0):
    #         if(nums[j] <= 0):
    #             sum = 0
    #         else:
    #             sum = nums[j]
    #         i+=1
    #     mx = max(mx, sum)
    #     j+=1
    # return mx

# nums = [-2,1,-3,4,-1,2,1,-5,4]
nums = [-1]
n = len(nums)
print(maxSubarray(nums,n))