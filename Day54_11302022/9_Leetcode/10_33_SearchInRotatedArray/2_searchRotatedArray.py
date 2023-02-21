# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# You must write an algorithm with O(log n) runtime complexity.

# Completed: TC passed
#Functions
def searchRotatedArray(nums, target):
    # 4 5 6 7 0 1 2; target = 0
    # n = 7//2 = 3; arr[3] = 7 = mid
    # start = 0 end = 6
    # 4 0 1 2 3 
    n = len(nums)
    start = 0
    end = n-1
    while(start<=end):
        mid = start + (end-start)//2 # mid 7
        if(nums[mid] == target):
            return mid
        # Left Check
        if(nums[start] <= nums[mid]):
            
            if target > nums[mid] or target<nums[start]: # modification in first condition
                start = mid+1
            else:
                end = mid-1
        else:
            #Right Check
            if target < nums[mid] or target > nums[end]: # Modification in this condition 
                end = mid-1
            else:
                start = mid+1
    return -1

# Driver Code
# nums = [4,5,6,7,0,1,2] 
nums = [1,3]
target = 3
print(searchRotatedArray(nums, target))