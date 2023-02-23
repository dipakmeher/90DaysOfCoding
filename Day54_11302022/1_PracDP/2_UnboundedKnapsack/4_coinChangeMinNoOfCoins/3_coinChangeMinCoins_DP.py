# Memorized: Coin Change Min no of ways
# Code is giving wrong result
import sys
# Function
def coinChangeMinCoins(coins, n, Sum):
    for j in range(Sum+1): 
        k[0][j] = sys.maxsize - 1 #coins[0][0]: we dont know to bring sum 0, we need how many coins... so infinity
    for i in range(1,n+1): # To Note: starts from 1
        k[i][0] = 0
    for j in range(1, Sum+1): # To Note: starts from 1
        if(j%coins[0] == 0):
            k[1][j] = Sum/coins[0] # To Note: We have to put divide here and not Modulus :(. Use Coins[0] because we are filling 1st row for coin[0]
        else:
            k[1][j] = sys.maxsize - 1

    for i in range(2,n+1):
        for j in range(1, Sum+1):
            if(coins[i-1]<=j):
                k[i][j] = min(1+k[i][j-coins[i-1]],k[i-1][j])
                print("k i,j = ", 1+k[i][j-coins[i-1]],k[i-1][j])
            else:
                k[i][j] = k[i-1][j]
    return k[n][Sum]


# Drivers Code
#coins = [9, 6, 5, 1]
coins = [1,3,5,7]
n = len(coins)
Sum = 18

k = [[sys.maxsize for j in range(Sum+1)] for i in range(n+1)]
print("Minimum coins required is",coinChangeMinCoins(coins, n, Sum))