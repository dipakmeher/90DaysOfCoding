# Egg Dropping Memorization
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
        tempAns = 1+ max(EggDropping(arr, e-1, k-1), EggDropping(arr, e, f-k))
        result = min(result, tempAns)
    dp[e][f] = result
    return result
# Drivers code
e = 2
f = 10
arr=[i for i in range(1,f+1)]
dp = [[-1 for j in range(f+1)] for i in range(e+1)]
print("Min no of attempts required to find the threshold is,", EggDropping(arr,e,f))