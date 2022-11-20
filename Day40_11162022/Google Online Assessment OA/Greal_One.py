INT_MAX = 100000000

# function to return the
# minimal number of moves
def minimalSteps(s, n):
    dp = [INT_MAX for i in range(n)]
    
    # initialize both strings to null
    s1 = ""
    s2 = ""
    
    # base case
    dp[0] = 1
    s1 += s[0]
    
    for i in range(1, n):
        s1 += s[i]
    
        # check if it can be appended
        s2 = s[i + 1: i + 1 + i + 1]
    
        # addition of character
        # takes one step
        dp[i] = min(dp[i], dp[i - 1] + 1)
    
        # appending takes 1 step, and
        # we directly reach index i*2+1
        # after appending so the number
        # of steps is stord in i*2+1
        if (s1 == s2):
            dp[i * 2 + 1] = min(dp[i] + 1,
                                dp[i * 2 + 1])
    
    return dp[n - 1]

res = minimalSteps("aabcc",5)
print("res = ",res)