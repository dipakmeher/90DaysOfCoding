# 0-1 Knapsack - DP
def knapSack0_1_DP(wt, val, W, n):
    K = [[0 for col in range(W+1)] for row in range(n+1)]
    # BC
    # n gets replaced with i and W gets replaced with w in loop
    for i in range(n+1):
        for w in range(W+1):
            if(n==0 or w==0):# corrected
                K[i][w] = 0# corrected
            # CD
            if(wt[n-1] <= w): # corrected
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]], K[i-1][w])# corrected
            else:
                K[i][w] = K[i-1][w]# corrected
    return K[n][W]

# Drivers Code
val = [60, 100, 120]
wt = [10, 20, 30]
n = len(wt)
W = 50

print("Max Profit (KS_ DP) = ", knapSack0_1_DP(wt, val, W, n))