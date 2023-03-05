#Coin change: Max number of ways problem
#Combination of Unbounded Knapsack + Count of Subset sum


def coinChagneMaxWays(Arr, n, Sum):
    for j in range(Sum+1):
        k[0][j] = 0
   
    for i in range(n+1):
        k[i][0] = 1

    for i in range(1,n+1): #Has to be start with 1,n+1
        for j in range(1,Sum+1):
            if(Arr[i-1]<=j):
                k[i][j] = k[i][j-Arr[i-1]] + k[i-1][j] #i: unbounded knapsack + subset sum
            else:
                k[i][j] = k[i-1][j]
    return k[n][Sum]

#Driver's Code
Arr = [1,2,3] # Coin Array
n = len(Arr)
Sum = 5

k = [[0 for i in range(Sum+1)] for j in range(n+1)]
print("Max number of ways to get the sum:",Sum,": with these coins are",coinChagneMaxWays(Arr, n, Sum))