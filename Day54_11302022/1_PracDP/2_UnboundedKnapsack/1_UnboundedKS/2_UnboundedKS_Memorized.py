# Unbounded Knapsack - Memorized
def knapSack0_1_M(wt, val, W, n):
    # BC
    if(n==0 or W==0):
        return 0
    if(K[n][W] != -1):
        return K[n][W]
    
    # CD
    if(wt[n-1] <= W):
        K[n][W] = max(val[n-1] + knapSack0_1_M(wt,val,W-wt[n-1], n), knapSack0_1_M(wt,val,W, n-1))
    else:
        K[n][W] = knapSack0_1_M(wt,val,W, n-1)
    return K[n][W]

# Drivers Code
val = [60, 100, 120]
wt = [10, 20, 30]
n = len(wt)
W = 50

K = [[-1 for col in range(W+1)] for row in range(n+1)]
print("Unbounded Max Profit (KS_ Memoized) = ", knapSack0_1_M(wt, val, W, n))