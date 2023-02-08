def lastOccurenceBS(arr, n, search):
    start = 0
    end = n-1

    while(start <= end):
        mid = start + (end-start)//2 # the last term is added to avoid overflow in worst case 4+4/2 = -3/2 if max = 4
        #whereas 4 + (4-4)/2 = 4
        if(arr[mid] == search):
            ans = mid # we dont know whether its a first occurence
            start = mid + 1
        if(search < arr[mid]):
            end = mid - 1
        else:
            start = mid + 1
    return ans

def firstOccurenceBS(arr, n, search):
    start = 0
    end = n-1

    while(start <= end):
        mid = start + (end-start)//2 # the last term is added to avoid overflow in worst case 4+4/2 = -3/2 if max = 4
        #whereas 4 + (4-4)/2 = 4
        if(arr[mid] == search):
            ans = mid # we dont know whether its a first occurence
            end = mid - 1
        elif(search < arr[mid]):
            end = mid - 1
        else:
            start = mid + 1
    return ans

#Driver code 
arr = [1,2,3,3,3,6,7] # this is an sorted array
n = len(arr)
k = 3
firstOccurence = firstOccurenceBS(arr, n, k)
lastOccurence = lastOccurenceBS(arr, n, k)
print(firstOccurence)
print(lastOccurence)

print("Count of the repeated element",k,"is,", lastOccurence-firstOccurence + 1)