# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.

# Status: Completed
def Sum3(nums, n):
    res = []
    nums.sort() # Negative element are at the beginning and Positive at the end
    for i,a in enumerate(nums):
        if(i>0 and a==nums[i-1]):
            continue
        l,r = i+1, len(nums) - 1
        # Now similar to Sliding Window Code
        while(l<r):
            Sum = a + nums[l] + nums[r]
            if(Sum > 0):
                r-=1
            elif(Sum<0):
                l+=1
            else:
                res.append([a,nums[l],nums[r]])
                l+=1
                while nums[l] == nums[l-1] and l<r:
                    l+=1
    return res


#Drivers Code
nums = [-1,0,1,2,-1,-4]
n = len(nums)

print(Sum3(nums,n))