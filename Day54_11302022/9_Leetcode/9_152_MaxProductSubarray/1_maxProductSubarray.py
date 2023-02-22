# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.

# Incomplete: Wrong Output
#Functions
def maxProductSubarray(nums):
    pos, neg, z, prod = 0,0,0,1
    for i in nums:
        if i<0:
            neg+=1
        elif(i>0):
            pos+=1
        else:
            z += 1
        prod = prod * i

    if neg>0 and z==0 and neg%2==0:
        return prod

    currPro,maxPro = 1,-11
    for i in nums:
        currPro = max(currPro * i, i)
        maxPro = max(currPro, maxPro)
    return maxPro

#Driver Code
# nums = [2,3,-2,4]
# nums = [-2,3,-4]
# nums = [-2,0,-1]
nums = [2,-5,-2,-4,3]
print(maxProductSubarray(nums))