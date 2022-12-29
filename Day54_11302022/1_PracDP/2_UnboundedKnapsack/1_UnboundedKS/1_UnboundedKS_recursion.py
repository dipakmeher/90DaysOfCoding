# Unbounded Knapsack - Recursive Code
def unboundedKnapSack(wt, val, W, n):
    # BC
    if(n==0 or W==0):
        return 0
    
    # CD
    if(wt[n-1] <= W):
        return max(val[n-1] + unboundedKnapSack(wt,val,W-wt[n-1], n), unboundedKnapSack(wt,val,W, n-1)) #Changes made here
    else:
        return unboundedKnapSack(wt,val,W, n-1)

# Drivers Code
val = [60, 100, 120]
wt = [10, 20, 30]
n = len(wt)
W = 50
print("Unbounded Max Profit(KS_Recursive) = ", unboundedKnapSack(wt, val, W, n)) # 10*5 = 60*5 = 300