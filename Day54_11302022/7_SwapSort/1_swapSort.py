# This technique can be used to solve the problem on non-static array in O(1) space
# 1 ro N array: Find the missing elements
# This problem can be done in 2 more ways: Usign HashMap and   

#Function
def swap(arr, a, b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp

def swapSort(arr, n):
    i = 0
    while(i<n):
        # We're basically checking whether the element is at correct place. If not then 
        # we're placing the ith element at its correct place.
        if(arr[i] != arr[arr[i]-1]):
            swap(arr, i, arr[i]-1) 
            # arr[i], arr[arr[i]-1] = arr[arr[i]-1], arr[i]
            # print("1", arr[i])
            # print("2", arr[arr[i]-1])
        else:
            i+=1
        print(arr)

    missing = []
    repeating = []
    for i in range(n):
        if(arr[i] != i+1):
            missing.append(i+1)
            repeating.append(arr[i])
    
    print("Missing elements: ", missing)
    print("Repeating elements: ", repeating)
    
    

#Driver Code
arr = [2,1,1,5,5]
n = len(arr)
swapSort(arr, n)