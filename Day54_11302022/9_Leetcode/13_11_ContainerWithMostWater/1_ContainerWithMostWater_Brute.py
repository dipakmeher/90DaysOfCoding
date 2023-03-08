# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

#TC: O(n*n)
#Function
def maxArea(height):
    res = 0
    for l in range(len(height)):
        for r in range(l+1, len(height)):
            temp = (r-l)*min(height[l],height[r])
            res = max(res,temp)
    return res


#Driver Code
height = [1,8,6,2,5,4,8,3,7]
print("Heights: \n",height)
print("MaxArea: ", maxArea(height))