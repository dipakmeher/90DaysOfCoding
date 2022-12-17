#Subset Sum Function: Memorized

def subsetSum(Arr, n, Sum):
    
    if(n==0 and Sum!=0): #Sum!=0 is an important step
        return False
    if(Sum == 0):
        return True
    
    if(k[n][Sum] != -1):
        return k[n][Sum]

    if(Arr[n-1]<=Sum):
        k[n][Sum] = (subsetSum(Arr, n-1, Sum-Arr[n-1]) or subsetSum(Arr, n-1, Sum))
        return k[n][Sum]
    else:
        k[n][Sum] = subsetSum(Arr, n-1, Sum)
        return k[n][Sum]

#Drivers Code
Arr = [3, 34, 4, 12, 5, 2]
n = len(Arr)
Sum = 9

k = [[-1 for i in range(Sum+1)] for j in range(n+1)]
print("Subset with the sum", Sum ,"exsits or not: ", subsetSum(Arr, n, Sum))