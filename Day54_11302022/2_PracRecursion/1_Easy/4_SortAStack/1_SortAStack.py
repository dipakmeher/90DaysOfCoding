#Sort a Stack using Recursion
from collections import deque
#funcion
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
    return
    #ID
def SortAStack(arr):
    #BC
    if(len(arr)==1):
        return 
    #HP
    temp = arr[len(arr)-1]
    arr.pop()
    SortAStack(arr)
    #ID
    insertTemp(arr, temp)

#Driver code
stack = deque(['1','2','5','3'])
print("Unsorted Stack: ", stack)
SortAStack(stack)
print("Sorted Stack: ", stack)