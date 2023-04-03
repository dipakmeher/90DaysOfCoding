# https://practice.geeksforgeeks.org/problems/find-the-position-of-m-th-item1723/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article

# Input : N = 5 // Size of circle
#         M = 2 // Number of items
#         K = 1 // Starting position

#G4G
#735/10102 Test Cases Passed
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