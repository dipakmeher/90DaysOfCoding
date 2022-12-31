# Josephus Problem
#Function
def josephusProblem(arr, k, index):
    if(len(arr)==1):
        print("Last person remained of position",arr[0])
        return

    index = (index+k)%len(arr)

    del arr[index]
    josephusProblem(arr,k,index)
     
    
#Driver Code
n = 7
k = 3
index = 0
arr = [i+1 for i in range(n)]
josephusProblem(arr, k-1, index)
