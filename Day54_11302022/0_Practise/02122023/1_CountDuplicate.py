#Using set on place of list has actually reduced the running time
def containsDuplicate(nums):
    hashSet = set()
    for i in nums:
        if i in hashSet:
            return True
        hashSet.add(i)
    return False

#Driver Code
nums = [1,2,3,4]
print(containsDuplicate(nums))