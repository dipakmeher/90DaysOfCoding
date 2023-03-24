#Functions
def eggDrop(n,k):

    if k == 0 or k==1:
        return k
    if n == 0:
        return k

    res = 100000
    for i in range(1, k+1):
        temp = 1 + max(eggDrop(n-1, i-1), eggDrop(n, k-i))
        res = min(res,temp)
    return res

#Drivers Code
n = 2
k = 10
print("Returning the minimum number of moves that you need to determine with certainty what the value of f is ",eggDrop(n,k))