#Subset Sum Function: DP Top Down
import sys
def subsetSum(Arr, n, Sum):
    
    for i in range(n+1):
        for j in range(Sum+1):
            if(i==0):
                k[0][j] = False
            # if(j == 0):
            #     k[i][0] = True
    for i in range(n+1):
        for j in range(Sum+1):
            if(j == 0):
                k[i][0] = True

    for i in range(1,n+1):
        for j in range(1,Sum+1):
            if(Arr[i-1]<=j):
                k[i][j] = (k[i-1][j-Arr[i-1]] or k[i-1][j])
            else:
                 k[i][j] = k[i-1][j]
    
    result = sys.maxsize  
    for j in range(Sum//2, -1, -1):
        if k[n][j] == True:
            result = Sum - (2*j)
            break

    return result

#Drivers Code

Arr = [1,2,7]
# Arr = [3, 1, 4, 2, 2, 1]
n = len(Arr)
Sum = 0
for i in range(n):
    Sum = Sum + Arr[i]

k = [[False for i in range(Sum+1)] for j in range(n+1)]
print("Subset with the sum", Sum ,"exsits or not: ", subsetSum(Arr, n, Sum))