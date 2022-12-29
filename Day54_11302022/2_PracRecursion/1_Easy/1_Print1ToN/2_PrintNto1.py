#Print the numbers from N to 1
#Function
def printNumber(n):
    #BC
    if(n==1):
        print(n)
        return
    #I
    print(n) # 7
    #HP
    printNumber(n-1) #1......6
    
#Driver Code
n = 7
printNumber(n)