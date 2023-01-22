#Subset Sum Function
# IBH, ip-op, decision tree 
def subsetSum(Arr, n, Sum):
    if(n==0 and Sum!=0): #Sum!=0 is an important step here to cover the edge case sum like 60
        return False
    if(Sum == 0):
        return True
    if(Arr[n-1]<=Sum):
        print("n-1: ", Arr[n-1])
        return (subsetSum(Arr, n-1, Sum-Arr[n-1]) or subsetSum(Arr, n-1, Sum))
    else:
        return subsetSum(Arr, n-1, Sum)

#Drivers Code
# Arr = [2,3,7,8,10]
# n = len(Arr)
# Sum = 30
Arr = [3, 34, 4, 12, 5, 2]
n = len(Arr)
Sum = 60

print("Subset with the sum", Sum ,"exsits or not: ", subsetSum(Arr, n, Sum))