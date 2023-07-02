# # Longest Common Substring LCS
# # Main Function
def LCSubstring(s1,s2,n,m, res):
    if(n==0 or m==0):
        # retuning res because we have to calculate the res and if 
        # don't return res then we are not considering the calcuation when s1=s2
        return res
    
    if(s1[n-1] == s2[m-1]):
        return LCSubstring(s1,s2,n-1, m-1, res+1)
    
    return max(res, max(LCSubstring(s1,s2,n-1, m, 0),LCSubstring(s1,s2,n, m-1, 0)))

# Drivers Code
s1 = "abcdgch"
s2 = "abxcdgchr"
n = len(s1)
m = len(s2)

print("The longest common substring for string s1 & s2 is,", LCSubstring(s1,s2,n,m, 0))

# Longest Common Subsequence LCS
# Main Function

# def LCSubstring(s1,s2,n,m,res):
#     if(n==0 or m==0):
#         return res
    
#     if(s1[n-1] == s2[m-1]):
#         res = 1+ LCSubstring(s1,s2,n-1, m-1, res+1)
        
#     return max(res,max(LCSubstring(s1,s2,n-1, m, 0),LCSubstring(s1,s2,n, m-1, 0)))

#         # If the character does not match then it won't be contigous anymore.
#     # return max(res, max(LCSubstring(s1,s2,n-1, m, 0),LCSubstring(s1,s2,n, m-1, 0)))
        
# # Drivers Code
# s1 = "abcdeefgh"
# s2 = "abxcdef"
# n = len(s1)
# m = len(s2)

# print("The longest common substring for string s1 & s2 is,", LCSubstring(s1,s2,n,m,0))