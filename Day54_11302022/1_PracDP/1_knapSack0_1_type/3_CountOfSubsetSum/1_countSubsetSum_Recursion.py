#Count Subset Sum Recursion

# Subset Sum Function
def countSubsetSum(Arr, n, Sum):
    if(n==0 and Sum!=0): #Sum!=0 is an important step here
        return 0
    if(Sum == 0):
        return 1
    if(Arr[n-1]<=Sum):
        return countSubsetSum(Arr, n-1, Sum-Arr[n-1]) + countSubsetSum(Arr, n-1, Sum)
    else:
        return countSubsetSum(Arr, n-1, Sum)

#Driver's Code
Arr = [3, 34, 4, 12, 5, 2]
n = len(Arr)
Sum = 9

print("Count of subset with sum", Sum ,"exsits or not: ", countSubsetSum(Arr, n, Sum))  