#Print the numbers from 1 to N
#Function
def printNumber(n):
    #BC
    if(n==1):
        print(n)
        return
    #HP
    printNumber(n-1) #1......6
    #I
    print(n) # 7
#Driver Code
n = 7
printNumber(n)