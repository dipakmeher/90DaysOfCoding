
#Function
def searchingIn2DArray(arr,n,m,k):
    i = 0
    j = m-1
    while(i>=0 and i<n and j<m and j>=0):
        if(arr[i][j] == k):
            return "yes"
        if(arr[i][j]>k):
            j = j - 1
        elif(arr[i][j]<k):
            i = i + 1
    return "No"
        
#Driver Code
arr = [[10, 20, 30, 40], [15, 25, 35, 45],
        [27, 29, 37, 48], [32, 33, 39, 50]]
# n&m are given
n = 4
m = 4
k = 29
print("Exist exist:", searchingIn2DArray(arr, n,m,k))