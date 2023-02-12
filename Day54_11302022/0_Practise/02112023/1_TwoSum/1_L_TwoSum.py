# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

#Functions
def twoSum(nums, n, Sum, ans):
    print("Sum: ", Sum)
    
    if(n==0 and Sum!=0):
        return 
    if(Sum == 0 and len(ans) == 2):
        return ans
   
    ans1 = ans
    ans2 = ans

    print("ans1 = ", ans1)
    print("ans2 = ", ans2)
    if(nums[n-1] <= Sum):
        ans1+=str(n-1)
        return twoSum(nums,n-1,Sum-nums[n-1], ans1) or twoSum(nums,n-1,Sum, ans2)
    else:
        return  twoSum(nums,n-1,Sum, ans2)
     
 
#Driver Code
nums = [2,7,11,15]
# nums = [-3,4,3,90]
n = len(nums)
target = 0
res = [int(i) for i in twoSum(nums, n, target,"")]
res.reverse()
print(res)
# res.reverse()
# print(res)