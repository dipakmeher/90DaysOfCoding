# Print Longest Common Subsequence 
# Main Function

def LCS(s1,s2,n,m, result):
    if(n==0 or m==0):
        return 0
    
    if(s1[n-1] == s2[m-1]):
        if(s1[n-1] not in result): # Can be done using this
            result.append(s1[n-1])
        return 1 + LCS(s1,s2,n-1, m-1, result)
    else:
        return max(LCS(s1,s2,n-1, m, result),LCS(s1,s2,n, m-1, result))
# Drivers Code
s1 = "abcdgh"
s2 = "abcdfr"
n = len(s1)
m = len(s2)
result = []
print("Print longest common subsequence for string s1 & s2 is, ", LCS(s1,s2,n,m, result))
print("Result: ","".join(result))