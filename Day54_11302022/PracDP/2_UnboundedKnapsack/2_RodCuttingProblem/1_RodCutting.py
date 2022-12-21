# RodCutting Problem
#This problem is same as Unbounded KS where wt[] = lenght[], Price[] = Profit[] and len = W

def RodCutting(Length, Price, n, len):
    K = [[0 for col in range(len+1)] for row in range(n+1)]
    # BC
    # n gets replaced with i and W gets replaced with w in loop
    for i in range(n+1):
        for w in range(len+1):
            if(i==0 or w==0):# corrected
                K[i][w] = 0# corrected
            # CD
            elif(Length[i-1] <= w): # corrected
                K[i][w] = max(Price[i-1] + K[i][w-Length[i-1]], K[i-1][w])# corrected
            else:
                K[i][w] = K[i-1][w]# corrected
    return K[n][len]

# Drivers Code
#Given
Price = [3,   5,   8,   9,  10,  17,  17,  20]
rlen = 8
#Let's make the array of Size 8
Length = [1,2,3,4,5,6,7,8]
n = len(Length)

#Now, the problem has been changed to Unbounded Knapsack

print("RodCutting Max Profit (KS_ DP) = ", RodCutting(Length, Price, n, rlen))