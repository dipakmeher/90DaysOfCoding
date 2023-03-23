# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.


# Functions
def findMin(nums):
    n = len(nums)
    start = 0 
    end = n - 1
    while(start<=end):
        mid = start + (end-start)//2
        #Need Two pointers
        prev = (mid-1+n)%n
        next = (mid+1)%n
        print(nums[mid])
        if(nums[mid]<=nums[prev] and nums[mid]<=nums[next]):
            return nums[mid]
        if(nums[start] < nums[end]):
            return nums[start]
        if(nums[start] <= nums[mid]):
            start = mid+1
        else:
            end = mid-1
#Drivers Code
nums = [3,4,5,1,2]
# nums = [4,5,6,7,0,1,2]
print(findMin(nums))