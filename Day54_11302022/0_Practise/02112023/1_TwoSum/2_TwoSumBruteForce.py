#Functions
def twoSum(nums, n, target):
    res = []
    for i in range(n):
        Sum  = 0
        Sum+= nums[i]
        for j in range(i+1, n):
            Sum+=nums[j]
            if(Sum == target):
                res.append(i)
                res.append(j)
            Sum-=nums[j]
    return res

#Driver Code
# nums = [2,7,11,15]
nums = [-3,4,3,90]
n = len(nums)
# target = 9
target = 0
print(twoSum(nums, n, target))