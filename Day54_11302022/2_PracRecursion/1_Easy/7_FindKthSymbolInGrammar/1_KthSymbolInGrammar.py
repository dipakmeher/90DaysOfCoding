# Find the kth symbol in grammar
# Function prototype
def kthSymbol(n,k):
    if n==1 and k==1:
        return 0
    mid = pow(2,n-1)//2
    if(k<=mid):
        return kthSymbol(n-1,k)
    else:
        if kthSymbol(n-1,k-mid) == 0:
            return 1
        else:
            return 0
# Driver code
#Grammar would be, Turn 0-> 01; 1-> 10
# 0
# 01
# 0110
# 0110 1001
n=4
k=3
print("Grammer(",n,",",k,") = ", kthSymbol(n,k))