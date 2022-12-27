# Egg Dropping Memorization Optimized
import sys
# function
def EggDropping(arr,e,f):
    result = sys.maxsize
    if f==0 or f==1:
        return f
    if e == 0:
        return f
    
    if(dp[e][f] != -1):
        return dp[e][f]

    for k in range(1, f+1): # If we take till f+1 then it will go till f
        if(dp[e-1][k-1] != -1):
            low =  dp[e-1][k-1]
        else:
            low = EggDropping(arr, e-1, k-1)
        
        if(dp[e][f-k] != -1):
            high =  dp[e][f-k]
        else:
            high = EggDropping(arr, e, f-k)

        tempAns = 1+ max(low, high)
        result = min(result, tempAns)
    dp[e][f] = result
    return result
# Drivers code
e = 2
f = 10
arr=[i for i in range(1,f+1)]
dp = [[-1 for j in range(f+1)] for i in range(e+1)]
print("Min no of attempts required to find the threshold is,", EggDropping(arr,e,f))