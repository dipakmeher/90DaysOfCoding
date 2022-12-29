# Min no of insertion and deletion to convert string a to b
# Main Function
def LCSInsDel(s1,s2,n,m):
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
s1 = "heap"
s2 = "pea"
n = len(s1)
m = len(s2)

k = [[0 for j in range(m+1)] for i in range(n+1)]
LCS = LCSInsDel(s1,s2,n,m)
insertion = m - LCS #Be careful, it's m in insertion
deletion = n - LCS #Be careful, it's n in deletion
print("Min no. of insertion and deletion to convert from string s1 to s2 is: Insertion: ",insertion,", Deletion:",deletion)