
#Function
def maxProductSubarray(nums):
    res = max(nums)
    currMax,currMin = 1, 1 # Because 1 is neutral
    n = len(nums)
    for i in nums:
        if i==0:
            currMax,currMin = 1, 1
            continue
        tmp = currMax * i # to get the previous currMax 
        currMax = max(currMax * i, currMin * i, i)
        currMin = min(tmp, currMin * i, i)
        res = max(currMax,res)
    return res

#Driver Code
# nums = [2,-5,-2,-4,3]
nums = [-2,0,-1]
print(maxProductSubarray(nums))

#  2 2 2 = 2 2 
#  -10 -10 -5 = -5; -10 -10 -5= -10 == -5 -10
# 10 20 -2 = 20; 10 20 -2 = -2 == 20 -2
# -80 8 -4== 8 -80
# 24 -240 3 == 24 -240