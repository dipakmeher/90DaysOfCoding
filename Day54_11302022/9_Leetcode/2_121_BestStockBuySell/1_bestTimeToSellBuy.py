# Best time to sell and buy stock
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

#Status: Time Limit Exceeded
# Function
def bestTimeBuySell(prices,n):
    maxProfit = 0
    for i in range(n):
        p = prices[i]
        for j in range(i+1,n):
            if(p>=prices[j]):
                continue
            tempProfit = prices[j]-p
            maxProfit = max(maxProfit,tempProfit)
    if(maxProfit>0):
        return maxProfit
    else:
        return 0


#Driver Code
prices = [7,1,5,3,6,4]
n = len(prices)
print(bestTimeBuySell(prices, n))