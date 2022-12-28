#Equal Sum Partition: DP

def subsetSum(Arr, n, Sum):
    global k
    for i in range(n+1):
        for j in range(Sum+1):
            if(i==0):
                k[0][j] = False
            # if(j == 0):
            #     k[i][0] = True
    for i in range(n+1):
        for j in range(Sum+1):
            if(j == 0):
                k[i][0] = True

    for i in range(1,n+1):
        for j in range(1,Sum+1):
            if(Arr[i-1]<=j):
                k[i][j] = (k[i-1][j-Arr[i-1]] or k[i-1][j])
            else:
                 k[i][j] = k[i-1][j]
    return k[n][Sum]

def EqualSumPartition(Arr,n):
    global k
    Range = sum(Arr)
    if(Range % 2 != 0): # i.e. not even
        return False
    else:  
        Sum = Range//2
        k = [[False for j in range(Sum+1)] for i in range(n+1)]
        return subsetSum(Arr,n,Sum)
#Drivers Code
# Arr = [2,3,7,8,10]
# n = len(Arr)
# Sum = 30

Arr = [3, 1, 5, 9, 12]
n = len(Arr)

k = []
print("Equal sum partition possible?:", EqualSumPartition(Arr, n))