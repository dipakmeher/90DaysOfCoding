
def bestTimeBuySell(prices, n):
    minprice = prices[0]
    profit = 0
    for i in prices:
        # Let's take advantage of stock has to be sold in future date
        if(i - minprice > profit):
            profit = i - minprice
        elif(i<minprice):
            minprice = i
    return profit


#Driver Code
prices = [7,1,5,3,6,4]
n = len(prices)
print(bestTimeBuySell(prices, n))