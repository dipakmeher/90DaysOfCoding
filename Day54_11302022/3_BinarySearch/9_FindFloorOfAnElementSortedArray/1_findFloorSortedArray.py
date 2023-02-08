def FloorbinarySearch(arr, n, search):
    start = 0
    end = n-1
    res = -1
    while(start <= end):
        mid = start + (end-start)//2 # the last term is added to avoid overflow in worst case 4+4/2 = -3/2 if max = 4
        #whereas 4 + (4-4)/2 = 4
        if(arr[mid] == search):
            res = arr[mid] 
            end = mid - 1
        elif(search < arr[mid]):
            end = mid - 1
        elif(arr[mid] < search):
            res = arr[mid]
            start = mid + 1
    return res
#Driver code 
arr = [1,2,3,4,6,7,8] # this is an sorted array
k=5 # floor
n = len(arr)
print("floor of element", k ,"in an array is",FloorbinarySearch(arr,n,k))