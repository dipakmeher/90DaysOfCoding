#Count Subset Sum Recursion

# Subset Sum Function
def countSubsetSum(Arr, n, Sum):
    if(n==0 and Sum!=0): #Sum!=0 is an important step here
        return 0
    if(Sum == 0):
        return 1
    if(k[n][Sum]!= -1):
        return k[n][Sum]

    if(Arr[n-1]<=Sum):
        k[n][Sum] = countSubsetSum(Arr, n-1, Sum-Arr[n-1]) + countSubsetSum(Arr, n-1, Sum)
        return k[n][Sum]
    else:
        k[n][Sum] = countSubsetSum(Arr, n-1, Sum)
        return k[n][Sum] 

#Driver's Code
Arr = [3, 34, 4, 12, 5, 2]
n = len(Arr)
Sum = 9

k = [[-1 for i in range(Sum+1)] for j in range(n+1)]
print("Count of subset with sum ",Sum," exsits or not: ",countSubsetSum(Arr, n, Sum))
print([[k[i][j] for j in range(Sum+1)] for i in range(n+1)])