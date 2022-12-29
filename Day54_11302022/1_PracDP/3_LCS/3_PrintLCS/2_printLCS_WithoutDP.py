# Print Longest Common Subsequence LCS
#Custom Soultion without using DP
# Main Function
def LCS(s1,s2,n,m):
    for i in range(n+1):
        for j in range(m+1):
            if i==0 or j==0:
                continue
            elif(s1[i-1] == s2[j-1]):
                result.append(s1[i-1])
    #         if i == 0 or j == 0:
    #             k[i][j] = 0
    #         elif(s1[i-1] == s2[j-1]):
    #             result.append(s1[i-1])
    #             k[i][j] = 1 + k[i-1][j-1]
    #         else:
    #             k[i][j] = max(k[i-1][j],k[i][j-1])
    # return k[n][m]
    return len(result)
# Drivers Code
s1 = "abcdgh" 
s2 = "abedgf"
n = len(s1)
m = len(s2)
result = []
print("The longest common subsequence for string s1 & s2 is, ", LCS(s1,s2,n,m))
print("Results: ", "".join(result))