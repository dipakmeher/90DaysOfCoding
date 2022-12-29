# Coin Change Min no of ways
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

    if(coins[n-1]<=Sum):
        return min(1+coinChangeMinCoins(coins,n, Sum-coins[n-1]),coinChangeMinCoins(coins, n-1, Sum))
    else:
        return coinChangeMinCoins(coins, n-1, Sum)


# Drivers Code
coins = [9, 6, 5, 1]
n = len(coins)
Sum = 13
print("Minimum coins required is",coinChangeMinCoins(coins, n, Sum))