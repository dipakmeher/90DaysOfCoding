# Input: Weight wt[], n, Value val[], n, W
# Asked: Find the max profit with the capcity W
# Output: max profit

#Function
def knapSack0_1(wt, val, n, W):
    #BC
    if(n==0 or W==0):
        return 0
    #Choice => Call on n-1
    if(wt[n-1] <= W):
        return max(val[n-1] + knapSack0_1(wt, val, n-1, W-wt[n-1]), knapSack0_1(wt, val, n-1, W)) #Mistake 1
    else:
        return knapSack0_1(wt, val, n-1, W)

#Driver Code
val = [60, 100, 120]
wt = [10, 20, 30]
n = len(wt)
W = 50
print("Max Profit(KS_Recursive) = ", knapSack0_1(wt, val, n, W))