# Longest Common Substring LCS
#Status: Incomplete
# Main Function
def LCSubstring(s1,s2,n,m):
    global mx
    global a
    if(n==0 or m==0):
        return 0
    
    if(s1[n-1] == s2[m-1]):
        a = 1+LCSubstring(s1,s2,n-1, m-1)
        # If the character does not match then it won't be contigous anymore.

    mx = max(a,max(LCSubstring(s1,s2,n-1, m),LCSubstring(s1,s2,n, m-1)))
    return mx
# Drivers Code
s1 = "abcdgch"
s2 = "abcdghr"
n = len(s1)
m = len(s2)
mx = 0
a=0
print("The longest common substring for string s1 & s2 is,", LCSubstring(s1,s2,n,m))