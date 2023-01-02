elif(arr[start] <= arr[mid]): # that means the first half array is sorted
            start = mid + 1
        elif(arr[mid] <= arr[end]):
            end = mid-1