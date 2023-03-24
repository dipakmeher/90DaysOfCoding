# https://practice.geeksforgeeks.org/problems/find-the-position-of-m-th-item1723/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article

# Input : N = 5 // Size of circle
#         M = 2 // Number of items
#         K = 1 // Starting position

#G4G
#All Test Cases Passed
#Function
def deliveredItem(n,m,k):
    a = (K+M-1)%N
    if(a==0):
        return N
    else:
        return a

#Drivers Code
N = 5 
M = 8
K = 2
print("Delivered Items",deliveredItem(N,M,K))