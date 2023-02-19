# Best time to sell and buy stock
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

#Status: Passed but more space
# Function
def bestTimeBuySell(prices,n):
    maxProfit = 0
    stack = []
    for i in range(n):
        if(len(stack) == 0):
            stack.append(prices[i])
        else:
            if(stack[-1]>prices[i]):
                stack.append(prices[i])
            elif(stack[-1]<prices[i]):
                tempProfit = prices[i]-stack[-1]
                maxProfit = max(maxProfit,tempProfit)
    if(maxProfit>0):
        return maxProfit
    else:
        return 0


#Driver Code
prices = [7,1,5,3,6,4]
n = len(prices)
print(bestTimeBuySell(prices, n))