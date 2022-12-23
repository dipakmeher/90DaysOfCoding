# Longest Common Subsequence LCS
# Main Function
def LCS(s1,s2,n,m):
    if(n==0 or m==0):
        return 0
    
    #Memorized Code
    if(k[n][m] != -1):
        return k[n][m]
    
    if(s1[n-1] == s2[m-1]):
        k[n][m] = 1 + LCS(s1,s2,n-1, m-1)
        return k[n][m]
    else:
        k[n][m] = max(LCS(s1,s2,n-1, m),LCS(s1,s2,n, m-1))
        return k[n][m]
# Drivers Code
s1 = "abcdgh"
s2 = "abedfr"
n = len(s1)
m = len(s2)

k = [[-1 for j in range(m+1)] for i in range(n+1)]
print("The longest common subsequence for string s1 & s2 is, ", LCS(s1,s2,n,m))