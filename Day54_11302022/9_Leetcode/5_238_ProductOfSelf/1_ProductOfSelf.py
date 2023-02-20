# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

#Function
def ProductOfSelf(nums, n):
    ans = []
    prefix = 1
    ans.append(prefix)
    for i in range(1,n):
        prefix = nums[i-1] * prefix
        ans.append(prefix)
    print("Prefix: :", ans)
    postfix = 1
    ans[n-1] = postfix * ans[n-1]
    for i in range(n-2,-1,-1): # -2 gives last second element and not n-1
        postfix = nums[i+1] * postfix
        ans[i] = postfix * ans[i]
    print("Postfix: :", ans)




#Drivers Code
nums = [1,2,3,4]
n = len(nums)
ProductOfSelf(nums, n)