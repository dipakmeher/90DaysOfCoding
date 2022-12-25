# MCM recursion
import sys
# function
def MCM(arr,i,j):
    result = sys.maxsize
    if i>=j:
        return 0
    for k in range(i, j): # If we take till j then it will go till j-1
        tempAns = MCM(arr, i, k) + MCM(arr, k+1, j) + arr[i-1]*arr[k]*arr[j]
        result = min(result, tempAns)
    return result
# Drivers code
arr = [1, 2, 3, 4, 3]
n = len(arr)

print("Min cost of MCM is,", MCM(arr,1, n-1))