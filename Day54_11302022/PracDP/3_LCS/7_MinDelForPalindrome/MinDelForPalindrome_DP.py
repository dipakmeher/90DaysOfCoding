# Min no of deletion to make string Pallindrome
# Main Function
def LPS(s1,s2,n,m):
    for i in range(n+1):
        for j in range(m+1):
            if i == 0 or j == 0:
                k[i][j] = 0
            elif(s1[i-1] == s2[j-1]):
                k[i][j] = 1 + k[i-1][j-1]
            else:
                k[i][j] = max(k[i-1][j],k[i][j-1])
    return k[n][m]  

# Drivers Code
s1 = "abcdba"
s2 = s1[::-1] # Imp steps in this code
n = len(s1)
m = len(s2)

k = [[0 for j in range(m+1)] for i in range(n+1)]
minDeletion = n - LPS(s1,s2,n,m) # Imp steps in this code
print("The longest pallindromic subsequence for string s1 & s2 is,", minDeletion)