#Subset Sum Function: DP Top Down

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
    return k[n][Sum]

#Drivers Code
# Arr = [2,3,7,8,10]
# n = len(Arr)
# Sum = 30

Arr = [3, 34, 4, 12, 5, 2]
n = len(Arr)
Sum = 37

k = [[False for i in range(Sum+1)] for j in range(n+1)]
print("Subset with the sum", Sum ,"exsits or not: ", subsetSum(Arr, n, Sum))