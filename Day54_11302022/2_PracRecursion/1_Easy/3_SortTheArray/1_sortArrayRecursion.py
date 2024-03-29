#Sort an array using recursion
#function
def insertTemp(arr, temp):
    #BC
    if(len(arr) == 0 or arr[len(arr) - 1] <= temp):
        arr.append(temp)
        return
    #HP
    val = arr[len(arr) - 1]
    arr.pop()
    insertTemp(arr, temp)
    arr.append(val)
    
    #ID
def SortArray(arr):
    #BC
    if(len(arr)==1):
        return 
    #HP
    temp = arr[len(arr)-1]
    arr.pop()
    SortArray(arr)
    #ID
    insertTemp(arr, temp)

#Driver code
arr = [5,4,3,1,2]
print("Unsorted list, ", arr)
SortArray(arr)
print("Sorted list, ", arr)