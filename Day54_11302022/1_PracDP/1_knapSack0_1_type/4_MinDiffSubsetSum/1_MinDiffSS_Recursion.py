#Minimum Subset Sum Difference

#Function

def MinDiffSubsetSum(Arr,n, SumCalc, Range):
    #Base Case
    if(n==0):
        return abs((Range - SumCalc)-SumCalc)

    return min(MinDiffSubsetSum(Arr, n-1, SumCalc + Arr[n-1], Range), MinDiffSubsetSum(Arr, n-1, SumCalc,Range))


def MinDiff(Arr, n):
    Range = 0
    for i in range(n):
        Range = Range + Arr[i]
    
    return MinDiffSubsetSum(Arr,n,0,Range)
#Drivers Code
Arr = [1,2,7]
n = len(Arr)
print("Min Sum Difference of Subset sum is: ",MinDiff(Arr, n))