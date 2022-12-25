# MCM DP
import sys
# function
def MCM(arr,i,j):
    result = sys.maxsize
    if i>=j:
        return 0
    if(dp[i][j] != -1):
        return dp[i][j]

    for k in range(i, j): # If we take till j then the loop will go till j-1
        tempAns = MCM(arr, i, k) + MCM(arr, k+1, j) + arr[i-1]*arr[k]*arr[j]
        result = min(result, tempAns)
    
    dp[i][j] = result
    return result

# Drivers code
arr = [1, 2, 3, 4, 3]
n = len(arr)
dp = [[-1 for j in range(n+1)] for i in range(n+1)]
print("Min cost of MCM is,", MCM(arr,1, n-1))