# 0-1 Knapsack - Recursive Code
def knapSack0_1(wt, val, W, n):
    # BC
    if(n==0 or W==0):
        return 0
    
    # CD
    if(wt[n-1] <= W):
        return max(val[n-1] + knapSack0_1(wt,val,W-wt[n-1], n-1), knapSack0_1(wt,val,W, n-1))
    else:
        return knapSack0_1(wt,val,W, n-1)

# Drivers Code
val = [60, 100, 120]
wt = [10, 20, 30]
n = len(wt)
W = 50
print("Max Profit(KS_Recursive) = ", knapSack0_1(wt, val, W, n)) 