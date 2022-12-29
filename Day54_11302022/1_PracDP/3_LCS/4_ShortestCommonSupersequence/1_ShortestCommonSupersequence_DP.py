# Shortest Common Supersequence LCS
# Main Function
def SCSupersequence(s1,s2,n,m):
    for i in range(n+1):
        for j in range(m+1):
            if i == 0 or j == 0:
                k[i][j] = 0
            elif(s1[i-1] == s2[j-1]):
                k[i][j] = 1 + k[i-1][j-1]
            else:
                k[i][j] = max(k[i-1][j],k[i][j-1])
    return n+m - k[n][m]
# Drivers Code
s1 = "abcdgh"
s2 = "abedfr"
n = len(s1)
m = len(s2)

k = [[0 for j in range(m+1)] for i in range(n+1)]
print("The shortest common supersequence for string s1 & s2 is,",SCSupersequence(s1,s2,n,m))