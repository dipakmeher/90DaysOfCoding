# Sequence Pattern Matching SPM
# Main Function

def SequencePM():
    varLCS = LCS(s1,s2,n,m)
    if varLCS == n:
        return True
    else:
        return False

def LCS(s1,s2,n,m):
    if(n==0 or m==0):
        return 0
    
    if(s1[n-1] == s2[m-1]):
        return 1 + LCS(s1,s2,n-1, m-1)
    else:
        return max(LCS(s1,s2,n-1, m),LCS(s1,s2,n, m-1))
# Drivers Code
s1 = "abc"
s2 = "abcdfr"
n = len(s1)
m = len(s2)

print("The sequence pattern mathcing for string s1 & s2 is,", SequencePM())