def binarySearchInInf(arr, n, search, start, end):
    while(start <= end):
        mid = start + (end-start)//2 # the last term is added to avoid overflow in worst case 4+4/2 = -3/2 if max = 4
        #whereas 4 + (4-4)/2 = 4
        if(arr[mid] == search):
            return mid
        if(search < arr[mid]):
            end = mid - 1
        else:
            start = mid + 1
#Driver code  
arr = [1,2,3,4,5,6,7,8,9] # this is an infinite sorted array
k=4 # Element to search
n = len(arr)

# Code to find start and end for infinite array
low = 0
high = 1
while(k>high): # this means the key is outside of start and end
    low = high
    high = high * 2

print("Position for the element", k ,"in an array is",binarySearchInInf(arr,n,k, low, high))