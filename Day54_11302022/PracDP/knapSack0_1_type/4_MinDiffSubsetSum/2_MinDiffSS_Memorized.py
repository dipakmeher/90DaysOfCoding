#Minimum Subset Sum Difference
# I guess Memorized can't be derived from the recursion here in this problem as of now
# But will try later

#Function

# def MinDiffSubsetSum(Arr,n, SumCalc, Range):
#     #Base Case
#     if(n==0):
#         return abs((Range - SumCalc)-SumCalc)
        
#     if(k[n][sum] != -1):
#         return k[n][Range]

#     k[n][Range] = min(MinDiffSubsetSum(Arr, n-1, SumCalc + Arr[n-1], Range), MinDiffSubsetSum(Arr, n-1, SumCalc,Range))
#     return k[n][Range] 


# #Drivers Code
# Arr = [1,2,7]
# n = len(Arr)
# Range = 0
# for i in range(n):
#     Range = Range + Arr[i]

# k = [[-1 for j in range(Range+1) for i in range(n+1)]]
# print("Min Sum Difference of Subset sum is: ",MinDiffSubsetSum(Arr,n,0,Range))