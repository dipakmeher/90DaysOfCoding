# Memorized: Coin Change Min no of ways
# Code is giving wrong result
import sys
# Function
def coinChangeMinCoins(coins, n, Sum):
    if n==0:
        #return minCoins = inf -1 
        return sys.maxsize - 1
    if n == 1:
        if(Sum%coins[n-1] == 0):
            return Sum/coins[n-1]
        else:
            return sys.maxsize - 1

    if(Sum == 0 and n !=0):
        return 0

    #Memorized Code
    if(k[n][Sum] != -1):
            return k[n][Sum]

    if(coins[n-1]<=Sum):
        k[n][Sum] = min(1+coinChangeMinCoins(coins,n, Sum-coins[n-1]),coinChangeMinCoins(coins, n-1, Sum))
        return k[n][Sum]
    else:
        k[n][Sum] = coinChangeMinCoins(coins, n-1, Sum)
        return k[n][Sum]


# Drivers Code
#coins = [9, 6, 5, 1]
coins = [1,3,5,7]
n = len(coins)
Sum = 18

k = [[-1 for j in range(Sum+1)] for i in range(n+1)]
print("Minimum coins required is",coinChangeMinCoins(coins, n, Sum))