# Egg Dropping recursion
import sys
# function
def EggDropping(arr,e,f):
    result = sys.maxsize
    if f==0 or f==1:
        return f
    if e == 0:
        return f
    
    for k in range(1, f+1): 
        tempAns = 1+ max(EggDropping(arr, e-1, k-1), EggDropping(arr, e, f-k))
        result = min(result, tempAns)
    return result
# Drivers code
e = 2
f = 10
arr=[i for i in range(1,f+1)]
print("Min no of attempts required to find the threshold is,", EggDropping(arr,e,f))