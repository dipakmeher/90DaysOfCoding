def MinDiffElebinarySearch(arr, n, search):
    start = 0
    end = n-1

    while(start <= end):
        mid = start + (end-start)//2 # the last term is added to avoid overflow in worst case 4+4/2 = -3/2 if max = 4
        #whereas 4 + (4-4)/2 = 4
        if(arr[mid] == search):
            return arr[mid]
        if(search < arr[mid]):
            end = mid - 1
        else:
            start = mid + 1
    if(abs(search-arr[end]) < abs(search-arr[start])):
        return arr[end]
    else:
        return arr[start]

#Driver code 
arr = [1,2,3,4,10,15] # this is an sorted array
k=12
n = len(arr)
print("Position for the Min Diff element", k ,"in an array is",MinDiffElebinarySearch(arr,n,k))