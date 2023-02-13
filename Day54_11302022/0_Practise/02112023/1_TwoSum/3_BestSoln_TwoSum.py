#Functions
def twoSum(nums, n, target):
    hashMap = {}
    res = []
    for i in range(n):
        a = target - nums[i]
        if a in hashMap:
            res.append(hashMap[a])
            res.append(i)
            break
        else:
            hashMap[nums[i]] = i
    return res

#Driver Code
nums = [2,7,11,15]
# nums = [-3,4,3,90]
n = len(nums)
target = 9
# target = 0
print(twoSum(nums, n, target))