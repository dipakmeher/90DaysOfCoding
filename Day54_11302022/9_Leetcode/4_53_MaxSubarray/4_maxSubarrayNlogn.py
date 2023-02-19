# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.

# TC: NLogN

def maxSubarray(nums,n):
    if(n==1):
        return nums[n-1]
    m = n//2
    left_MSS = maxSubarray(nums[:m],m)
    right_MSS = maxSubarray(nums[m:],n-m)
    print("LeftMSS: ",nums[:m], left_MSS)
    print("rightMSS", nums[m:], right_MSS)
    leftSum = -100000 
    rightSum = -100000
    sum = 0
    # Max in Right Sum
    for i in range(m, n):
        sum = sum + nums[i]
        rightSum = max(sum, rightSum)
    sum = 0
    for j in range(m-1,-1,-1):
        sum = sum+nums[j]
        leftSum = max(sum,leftSum)
    print("rightSum: ",rightSum)
    print("leftSum: ",leftSum)
    ans = max(left_MSS, right_MSS)
    print("Max: ",max(ans, leftSum + rightSum))
    return max(ans, leftSum + rightSum)


nums = [-2,1,-3,4,-1,2,1,-5,4]
# nums = [-1]
# nums = [5,4,-1,7,8]
n = len(nums)
print(5//2)
print(maxSubarray(nums,n))