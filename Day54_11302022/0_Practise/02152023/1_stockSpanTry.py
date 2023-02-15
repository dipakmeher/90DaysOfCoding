# Stock Span Problem
# Input: N = 7, price[] = [100 80 60 70 60 75 85]
# Output: 1 1 1 2 1 4 6
# We have made use of stack here because we have to traverse through array 
# in from current element to start order to check the condition and 
# that too for each element
# So it would be easier to use stack that gives us the previous element 
# using stack.top()
def stockSpanProblem(res):
    for i in range(0,len(res)):
        res[i] = i - res[i]
    return res
def nearestGreatestElementLeft(n, arr):
    stack = []
    for i in range(0, n):
        if(len(stack) == 0):
            res.append(-1)
        elif(len(stack) > 0 and stack[-1][0]>arr[i]):
            res.append(stack[-1][1])
        elif(len(stack) > 0 and stack[-1][0]<=arr[i]):
            while(len(stack) > 0 and stack[-1][0]<=arr[i]):
                stack.pop()
            if(len(stack) == 0):
                res.append(-1)
            else:
                res.append(stack[-1][1])
        stack.append([arr[i],i])

daily_price = 7
price = [100, 80, 60, 70, 60, 75, 85]
res = []
nearestGreatestElementLeft(daily_price, price)
print("Before StockSpan: ",res)
print("After StockSpan = ",stockSpanProblem(res))