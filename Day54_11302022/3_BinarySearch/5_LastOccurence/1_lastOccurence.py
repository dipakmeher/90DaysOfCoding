def lastOccurenceBS(arr, n, search):
    start = 0
    end = n-1

    while(start <= end):
        mid = start + (end-start)//2 # the last term is added to avoid overflow in worst case 4+4/2 = -3/2 if max = 4
        #whereas 4 + (4-4)/2 = 4
        if(arr[mid] == search):
            ans = mid # we dont know whether its a first occurence
            start = mid + 1 # The only change from FirstOccurenceOfLetterCode
        if(search < arr[mid]):
            end = mid - 1
        else:
            start = mid + 1
    return ans # we return the element at the end
#Driver code 
arr = [1,2,3,3,3,6,7] # this is an sorted array
k=3
n = len(arr)
print("Last occurence of an element", k ,"in an array is",lastOccurenceBS(arr,n,k))