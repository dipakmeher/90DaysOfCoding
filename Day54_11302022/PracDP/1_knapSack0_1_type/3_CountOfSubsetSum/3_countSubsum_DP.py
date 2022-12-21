#Count Subset Sum Recursion

# Subset Sum Function
def countSubsetSum(Arr, n, Sum):
    for i in range(n+1):
        for j in range(Sum+1):
            if(i==0): #Sum!=0 is an important step here
                k[0][j] = 0
   
    for i in range(n+1):
        for j in range(Sum+1):
            if(j == 0):
                k[i][0] = 1

    for i in range(1,n+1): #Has to be start with 1,n+1
        for j in range(1,Sum+1):
            if(Arr[i-1]<=j):
                k[i][j] = k[i-1][j-Arr[i-1]] + k[i-1][j]
            else:
                k[i][j] = k[i-1][j]
    return k[n][Sum]

#Driver's Code
Arr = [3, 34, 4, 12, 5, 2]
n = len(Arr)
Sum = 9

k = [[0 for i in range(Sum+1)] for j in range(n+1)]
print("Count of subset with sum ",Sum," :",countSubsetSum(Arr, n, Sum))
print([[k[i][j] for j in range(Sum+1)] for i in range(n+1)])