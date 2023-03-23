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
# def largestSubgrid(grid, maxSum): 
#     def get_area(top_i, left_j, size): 
#             return pre_sum[top_i + size][left_j + size] - pre_sum[top_i + size][left_j] - pre_sum[top_i][left_j + size] + pre_sum[top_i][left_j] 
#         n = len(grid) 
#         pre_sum = [[0] * (n + 1) for i in range(n + 1)] 
#         for i in range(n): 
#             for j in range(n): 
#                 pre_sum[i + 1][j + 1] = grid[i][j] + pre_sum[i + 1][j] + pre_sum[i][j + 1] - pre_sum[i][j] 
#         size = n 
#         for i in range(n): 
#             for j in range(n): 
#                 if i + size > n or j + size > n: 
#                     continue 
#                 while size > 0 and get_area(i, j, size) > maxSum: 
#                     size -= 1 
#         return size