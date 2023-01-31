# Josephus Problem
#Function
def josephusProblem(arr, k, index):
    if(len(arr)==1):
        print("Last person remained of position",arr[0])
        return

    index = (index+k)%len(arr)

    del arr[index]
    josephusProblem(arr,k,index) # Remember k is not been decremented
     
    
#Driver Code
n = 7 # Total number of people
k = 3 # k represents the number of jumps to take from index
index = 0
arr = [i+1 for i in range(n)]
josephusProblem(arr, k-1, index)
