# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.

# Status: Incomplete Not able to eliminate duplicates
def Sum3(nums, n):
    res = []
    if(len(nums)<=3):
        return res
    
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1, n):
                tempRes = []
                if(i!=j and j!=k and k!=i and nums[i] + nums[j] + nums[k] == 0):
                    tempRes.append(nums[i])
                    tempRes.append(nums[j])
                    tempRes.append(nums[k])
                if(len(tempRes)>0 and len(tempRes) == 3):
                    res.append(tempRes)
    return res


#Drivers Code
nums = [-1,0,1,2,-1,-4]
n = len(nums)

print(Sum3(nums,n))