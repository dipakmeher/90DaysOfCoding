#https://practice.geeksforgeeks.org/problems/stock-buy-and-sell2615/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article

# 1 Test Case Passed
#Functions
def buySellStocks(price,n):
    i = 0
    res = list()
    while(i<n-1):
        #Find local minima
        while((i<n-1) and (price[i+1] <= price[i])):
            i+=1
        if(i == n-1):
            break
        res.append(i)
        i+=1

        #Find local maxima
        while((i<n) and (price[i] >= price[i-1])):
            i+=1
        res.append(i-1)
    for i in range(1,len(res),2):
        print("(",res[i-1],"",res[i],")", end="")


#DriversCode
# stock = [100,180,260,310, 40, 535, 695]
stock = [23, 13, 25, 29, 33, 19, 34, 45, 65, 67]
n = len(stock)
buySellStocks(stock,n)
