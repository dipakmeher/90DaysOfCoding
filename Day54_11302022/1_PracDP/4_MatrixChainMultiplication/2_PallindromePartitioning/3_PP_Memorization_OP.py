# Palindrome Partitioning Optimized
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
    if(dp[i][j] != -1):
        return dp[i][j]
    for k in range(i, j): # If we take till j then it will go till j-1
        if(dp[i][k] != -1):
            left =  dp[i][k]
        else:
            left = PPartitioning(s1, i, k)
        
        if(dp[k+1][j] != -1):
            right =  dp[k+1][j]
        else:
            right = PPartitioning(s1, k+1, j)
        tempAns = left + right + 1 # 1 is for counting the current partition
        result = min(result, tempAns)
    dp[i][j] = result
    return result
# Drivers code
s1 = "nitin"
n = len(s1)
dp = [[-1 for j in range(n+1)] for i in range(n+1)]
print("Min cost of MCM is,", PPartitioning(s1,0, n-1)) # Note i should be 0 always