#Subset Sum Function: DP Top Down

# Subset Sum Function
def countSubsetSumDiff(Arr, n, Sum):
    for i in range(n+1):
        for j in range(Sum+1):
            if(i==0 and j!=0): #Sum!=0 is an important step here
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

#Drivers Code
# Arr = [2,3,7,8,10]
# n = len(Arr)
# Sum = 30

Arr = [1, 1, 2, 3]
n = len(Arr)
diff = 1
Range = sum(Arr)
print("Sum: ", Range)
# s2-s1 = diff
# R-2s1 = diff>> s1 = R-diff //2 : If one sum exist then other part of sum does exist 
Sum = (Range - diff)//2
# Basically we are finding, how many subsets are possible to bring the Sum using these array elements
k = [[0 for i in range(Sum+1)] for j in range(n+1)]
print("Total count of subset sum with difference ",diff," is: ", countSubsetSumDiff(Arr, n, Sum))