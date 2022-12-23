# Longest Common Substring LCS
#Status: Incomplete
# Main Function
def LCSubstring(s1,s2,n,m):
    if(n==0 or m==0):
        return 0
    
    if(s1[n-1] == s2[m-1]):
        return 1 + LCSubstring(s1,s2,n-1, m-1)
    else:
        return 0 # If the character does not match then it won't be contigous anymore.

# Drivers Code
s1 = "abcdgh"
s2 = "abedfr"
n = len(s1)
m = len(s2)

print("The longest common subsequence for string s1 & s2 is,", LCSubstring(s1,s2,n,m))