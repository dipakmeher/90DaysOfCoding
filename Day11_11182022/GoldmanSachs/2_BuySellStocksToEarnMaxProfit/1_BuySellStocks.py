#https://practice.geeksforgeeks.org/problems/stock-buy-and-sell2615/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article
# doing that, continuing
#Functions 
def buySellStocks(stock):
    i = 0
    j = i+1

    mp = 0
    total = 0
    while(j<len(stock)):
        if(stock[j]>stock[i] and stock[j]>stock[j-1]):
            print(stock[j]," - ", stock[i])
            mp = stock[j] - stock[i]
        else:
            print("Total: ",stock[j]," - ", stock[i])
            i = j
            total = total + mp
            print("Total: ", total)
        j+=1
    total = total+mp
    return total

#DriversCode
stock = [100,180,260,310, 40, 535, 695]
print("MaxProfit: ", buySellStocks(stock))
