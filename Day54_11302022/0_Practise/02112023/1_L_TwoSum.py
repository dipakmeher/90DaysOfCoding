# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

#Functions
def twoSum(nums, n, Sum, ans):
    print("Sum: ", Sum)
    
    if(n==0 and Sum!=0):
        return -1
    if(Sum == 0 and len(ans) == 2):
        return ans
    if(n==0):
         return ans
    ans1 = ans
    ans2 = ans

    print("ans1 = ", ans1)
    print("ans2 = ", ans2)
    if(nums[n-1] <= Sum):
        twoSum(nums,n-1,Sum-nums[n-1], ans1) 
    else:
        twoSum(nums,n-1,Sum, ans2)
    #return ans
 
#Driver Code
nums = [3,2,3]
n = len(nums)
target = 6
print(twoSum(nums, n, target, []))
# res.reverse()
# print(res)