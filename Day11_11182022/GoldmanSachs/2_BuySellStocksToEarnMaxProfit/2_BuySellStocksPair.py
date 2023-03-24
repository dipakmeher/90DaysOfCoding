#https://practice.geeksforgeeks.org/problems/stock-buy-and-sell2615/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article

# 1 Test Case Passed
#Functions
def buySellStocks(price):
    i = 0
    j = i+1

    mp = 0
    res = []
    while(j<len(price)):
        if(price[j]>price[i] and price[j]>price[j-1]):
            print(price[j]," - ", price[i])
            mp = price[j] - price[i]
        else:
            print("Total: ",price[j]," - ", price[i])
            res.append([price[i], price[j-1]])
            i = j
            
        j+=1
    res.append([price[i], price[j-1]])
    if(len(res) == 0):
        print("No Profit")
    else:
        for rec in res:
            print("(",rec[0],"",rec[1],")", end="")

#DriversCode
stock = [100,180,260,310, 40, 535, 695]
print("MaxProfit: ", buySellStocks(stock))
