def peakElement(arr, n):
    start = 0
    end = n-1
    while(start <= end):
        mid = start + (end-start)//2 # the last term is added to avoid overflow in worst case 4+4/2 = -3/2 if max = 4
        #whereas 4 + (4-4)/2 = 4
        if(arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]):
            res.append(arr[mid])
            return mid
        elif(arr[mid] < arr[mid-1]):
            end = mid - 1
        elif(arr[mid] < arr[mid+1]):
            start = mid + 1
        elif(mid == 0):
            if(arr[0]>arr[1]):
                res.append(arr[0])
                return 0
            else:
                res.append(arr[1])
                return 1
        if(mid == n-1):
            if(arr[n-1]>arr[n-2]):
                res.append(arr[n-1])
                return n-1
            else:
                res.append(arr[n-2])
                return n-2
        
#Driver code 
arr = [1,3,2,5,10,20,15] # this is an unsorted array and there's only one peak element in an array  
n = len(arr)
res = []
print("Position for the element in an array is",arr[peakElement(arr,n)])
print(res)

#Same Variations:
#Biotonic array:find max element
