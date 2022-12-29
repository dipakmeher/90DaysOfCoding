# Shortest Common Supersequence: Recursion
# Main Function

def SCSupersequence(s1,s2,n,m):
    if(n==0):
        return m
    if(m==0):
        return n
    
    if(s1[n-1] == s2[m-1]):
        return 1 + SCSupersequence(s1,s2,n-1, m-1)
    else:
        return 1 + min(SCSupersequence(s1,s2,n-1, m),SCSupersequence(s1,s2,n, m-1))
# Drivers Code
s1 = "abcdgh"
s2 = "abedfr"
n = len(s1)
m = len(s2)
print("The longest common subsequence for string s1 & s2 is, ", SCSupersequence(s1,s2,n,m))