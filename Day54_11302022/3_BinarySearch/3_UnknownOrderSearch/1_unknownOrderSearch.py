#Sorted means Binary Search
def ascendingBS(arr, n, search):
    start = 0
    end = n-1
    while(start <= end):
        mid = start + (end-start)//2 # the last term is added to avoid overflow in worst case 4+4/2 = -3/2 if max = 4
        #whereas 4 + (4-4)/2 = 4
        if(arr[mid] == search):
            return mid
        if(search < arr[mid]):
            end = mid - 1
        else:
            start = mid + 1
def decBinarySearch(arr, n, search):
    start = 0
    end = n-1
    while(start <= end):
        mid = start + (end-start)//2 # the last term is added to avoid overflow in worst case 4+4/2 = -3/2 if max = 4
        #whereas 4 + (4-4)/2 = 4
        if(arr[mid] == search):
            return mid
        if(search < arr[mid]):
            start = mid + 1
        else:
            end = mid - 1

def UnknownBinarySearch(arr, n ,k):
    if(n==1):
        if(arr[0] == k):
            return 0
    if(arr[0]<arr[1]):
        res = ascendingBS(arr, n, k)
    else:
        res = decBinarySearch(arr, n, k)
    return res

#Driver code 
arr = [1,2,3,4,5,6,7] # this is an sorted array
k = 2 # element to be searched
n = len(arr)

print("Position for the element", k ,"in an array is",UnknownBinarySearch(arr,n,k))