# Palindrome Partitioning recursion
import sys
# function
def isPalindrome(s1,i,j):
    while(i<=j):
        if(s1[i] != s1[j]):
            return 0
        i += 1
        j -= 1
    return 1

def PPartitioning(s1,i,j):
    result = sys.maxsize
    if i>=j:
        return 0
    if isPalindrome(s1, i, j):
        return 0
    for k in range(i, j): # If we take till j then it will go till j-1
        tempAns = PPartitioning(s1, i, k) + PPartitioning(s1, k+1, j) + 1 # 1 is for counting the current partition
        result = min(result, tempAns)
    return result
# Drivers code
s1 = "nitin"
n = len(s1)

print("Min cost of MCM is,", PPartitioning(s1,0, n-1)) # Note i should be 0