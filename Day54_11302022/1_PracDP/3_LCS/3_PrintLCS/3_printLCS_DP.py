# Print Longest Common Subsequence LCS
#Custom Soultion without using DP
# Main Function
def LCS(s1,s2,n,m):
    for i in range(n+1):
        for j in range(m+1):
            if i == 0 or j == 0:
                k[i][j] = 0
            elif(s1[i-1] == s2[j-1]):
                k[i][j] = 1 + k[i-1][j-1]
            else:
                k[i][j] = max(k[i-1][j],k[i][j-1])

    i = n
    j = m

    while(i>0 and j>0):
        if(s1[i-1] == s2[j-1]):
            result.append(s1[i-1])
            i = i-1
            j = j-1
        else:
            if(k[i-1][j]>k[i][j-1]):
                i = i - 1
            else: 
                j = j - 1
        
    return "".join(result[::-1])

# Drivers Code
s1 = "abcdgh" 
s2 = "abedgf"
n = len(s1)
m = len(s2)
result = []
k = [[0 for j in range(m+1)] for i in range(n+1)]
print("The longest common subsequence for string s1 & s2 is, ", LCS(s1,s2,n,m))