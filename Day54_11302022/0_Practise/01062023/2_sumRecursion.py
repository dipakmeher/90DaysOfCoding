def sumNat(n):
    if n==1:
        return 1
    return n+sumNat(n-1)

print("Sum of natural numbers: ", sumNat(5))
#1,2,3,4,5