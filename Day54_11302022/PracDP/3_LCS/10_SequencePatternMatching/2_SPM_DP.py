# Sequence Pattern Matching SPM

def SequencePM():
    varLCS = LCS(s1,s2,n,m)
    if varLCS == n:
        return True
    else:
        return False
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
    return k[n][m]
# Drivers Code
s1 = "abc"
s2 = "abcdfr"
n = len(s1)
m = len(s2)

k = [[0 for j in range(m+1)] for i in range(n+1)]
print("The longest common subsequence for string s1 & s2 is,", SequencePM())