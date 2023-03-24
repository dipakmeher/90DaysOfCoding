# Input : N = 5 // Size of circle
#         M = 2 // Number of items
#         K = 1 // Starting position

#G4G
#735/10102
#Function
def deliveredItem(n,m,k):
    # nlist = [i for i in range(1,n+1)]
    i=k
    while(i<=n):
        m-=1
        if(m == 0):
            return i
        i+=1
        i=i%n

#Drivers Code
N = 5 
M = 8
K = 2
print("Delivered Items",deliveredItem(N,M,K))