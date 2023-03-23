# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.


# Functions
def findMin(nums):
    l, r = 0, len(nums) - 1

    while l < r:
        m = l + (r - l) // 2

        if nums[m] > nums[r]:
            # We know that the pivot must be to the right
            # 4 5 6 7 8 9 10 0 1 2 3
            #           m
            l = m + 1
            
        else:
                # We know that we're at the pivot, or the pivot is to the left
                r = m 

    return nums[l]
#Drivers Code
nums = [3,4,5,1,2]
# nums = [4,5,6,7,0,1,2]
print(findMin(nums))