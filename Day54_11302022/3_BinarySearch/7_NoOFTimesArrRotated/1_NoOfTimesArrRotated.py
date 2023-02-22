def RotatedArray(arr, n):
    start = 0
    end = n-1
    while(start <= end):
        mid = start + (end-start)//2 # the last term is added to avoid overflow in worst case 4+4/2 = -3/2 if max = 4
        #whereas 4 + (4-4)/2 = 4
        prev = (mid + n - 1)%n # if mid = 0  then mid-1 would be negative
        next = (mid + 1)%n 
        print("Mid: ",mid)
        print("start: ",start)
        print("end: ",end)
        if(arr[mid] <= arr[prev] and arr[mid] <= arr[next]):
            print(mid)
            return mid
        if(arr[start] <= arr[mid]): # that means the first half array is sorted
            start = mid + 1
        elif(arr[mid] <= arr[end]):
            end = mid-1
        # elif(arr[mid] < arr[start]):
        #     end = mid - 1
        # elif(arr[mid] > arr[end]):
        #     start = mid +1
    
#Driver code 
arr = [15, 18, 2, 3, 6, 12, 13] # this is an sorted array
n = len(arr) 
print("Arr rotated for ", RotatedArray(arr,n))

# Following code can be done using above code with little variation
# Find the element in rotated sorted array

