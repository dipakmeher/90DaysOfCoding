# Longest Common Substring DP
# Status: Incomplete
# Main Function
def LCSubstring(s1,s2,n,m):
    result = 0
    for i in range(n+1):
        for j in range(m+1):
            if i == 0 or j == 0:
                k[i][j] = 0
            elif(s1[i-1] == s2[j-1]):
                k[i][j] = 1 + k[i-1][j-1]
                result = max(result, k[i][j])
            else:
                k[i][j] = 0
    return result
# Drivers Code
s1 = "abcdgh"
s2 = "abcdfr"
n = len(s1)
m = len(s2)

k = [[0 for j in range(m+1)] for i in range(n+1)]
print("The longest common Sub_string for string s1 & s2 is, ",LCSubstring(s1,s2,n,m))