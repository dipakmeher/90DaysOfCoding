# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# You must write an algorithm with O(log n) runtime complexity.

#Functions
def searchRotatedArray(nums, target):
   # find the pivot
    l=0
    r=len(nums)-1
    while l<=r:
        mid=(l+r)//2
        if nums[mid]==target:
            return mid
        if nums[l]<=nums[mid]:
            if target>=nums[l] and target<=nums[mid]:
                r=mid-1
            else:
                l=mid+1
        else:
            if target>nums[mid] and target<=nums[r]:
                l=mid+1
            else:
                r=mid-1
    return -1
# Driver Code
# nums = [4,5,6,7,0,1,2] 
nums = [1,3]
target = 3
print(searchRotatedArray(nums, target))


