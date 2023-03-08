# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

#TC: O(n)
#Function
def maxArea(height):
    n = len(height)
    l = 0
    r = n-1
    res = 0
    while l<r:
        temp = (r-l) * min(height[l],height[r])
        res = max(res,temp)

        if(height[l]<height[r]):
            l+=1
        elif(height[l]>height[r]):
            r-=1
        else:
            r-=1
    return res


#Driver Code
height = [1,8,6,2,5,4,8,3,7]
print("Heights: \n",height)
print("MaxArea: ", maxArea(height))