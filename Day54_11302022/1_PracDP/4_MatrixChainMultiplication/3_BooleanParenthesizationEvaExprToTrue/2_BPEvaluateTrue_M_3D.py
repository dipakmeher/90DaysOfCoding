# Boolean Parenthesization using Map
import sys
# function
def BPEvaluateTrue(arr,i,j, isTrue):
    result  = 0
    if i>j:
        return False

    if i==j:
        if(isTrue == 1):
            return arr[i] == "T" # Imp step to note
        else:
            return arr[i] == "F" # Imp step to note

    if(dp[i][j][isTrue] != -1):
        return dp[i][j][isTrue]

    for k in range(i+1 , j ,2): # If we take till j then it will go till j-1
        lt = BPEvaluateTrue(arr,i,k-1, 1)
        rt = BPEvaluateTrue(arr,k+1,j, 1)
        lf = BPEvaluateTrue(arr,i,k-1, 0)
        rf = BPEvaluateTrue(arr,k+1,j, 0)

        if(arr[k] == "&"):
            if(isTrue == 1):
                result = result + lt*rt 
            else:
                result = result + lt*rf + lf*rt + lf*rf
        
        if(arr[k] == "|"):
            if(isTrue == 1):
                result = result + lt*rt + lt*rf + lf*rt
            else:
                result = result + lf*rf

        if(arr[k] == "^"):
            if(isTrue == 1):
                result = result + lt*rf + lf*rt  
            else:
                result = result + lf*rf + lt*rt

    dp[i][j][isTrue] = result
    return dp[i][j][isTrue]
# Drivers code
arr = "T^F&T"
n = len(arr)

dp = [[[-1 for flag in range(2)] for j in range(n+1)] for i in range(n+1)]
print("Total count to evaluate expression to True is,", BPEvaluateTrue(arr,0, n-1, 1))
#MCM(arr, i, j, isTrue)