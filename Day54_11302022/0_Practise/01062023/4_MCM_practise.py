# MCM
import sys
#Functions
def MCM_Practise(arr, i, j):
    result = sys.maxsize #since we want the min value here
    if i>=j:
        return 0
    for k in range(i, j): # We are taking till j(n-1) because we dont want the empty separations there
        tempAns = MCM_Practise(arr,i,k) + MCM_Practise(arr, k+1, j) + arr[i-1]*arr[k]*arr[j]
        result = min(result, tempAns)
    return result

#Drive Code
arr = [1, 2, 3, 4, 3]
n = len(arr)
# i=1 because it is valid start point for multiplication 
#j = n-1 because it is a valid end point that does not give the empty distribution in recurison call at any time 
# Basically we want to ensure that for the first call atleast there is no empty recursive call. That's how we make the distribution for recurison call 
print("Min cost MCM is ",MCM_Practise(arr, 1,n-1))
