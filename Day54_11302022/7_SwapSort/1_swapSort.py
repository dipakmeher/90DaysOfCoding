

#Function
def swap(arr, a, b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp

def swapSort(arr, n):
    i = 0
    while(i<n):
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