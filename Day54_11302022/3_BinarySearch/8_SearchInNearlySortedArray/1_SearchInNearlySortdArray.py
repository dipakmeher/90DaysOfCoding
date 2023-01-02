def binarySearchNearly(arr, n, search):
    start = 0
    end = n-1
    while(start <= end):
        mid = start + (end-start)//2 # the last term is added to avoid overflow in worst case 4+4/2 = -3/2 if max = 4
        #whereas 4 + (4-4)/2 = 4
        if(arr[mid] == search):
            return mid

        if(mid-1>=start and arr[mid-1] == search):
            return mid -1
        
        if(mid+1<=end and arr[mid+1] == search):
            return mid + 1

        if(search < arr[mid]):
            end = mid - 1
        else:
            start = mid + 1
#Driver code 
arr = [5,10,30,20,40] # this is an nearly sorted array where the elements are swapped in between
k  = 20
n = len(arr)
print("Element is on index",binarySearchNearly(arr,n,k))