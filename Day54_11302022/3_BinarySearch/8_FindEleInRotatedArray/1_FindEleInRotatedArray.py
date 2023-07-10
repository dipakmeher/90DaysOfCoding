def RotatedArray(arr,n):
    start = 0
    end = n-1
    while(start<=end):
        mid = start + (end-start)//2
        prev  = (mid + n + 1)%n
        next = (mid+1)%n
        if(arr[mid]<=arr[prev] and arr[mid]<=arr[next]):
            return mid
        if(arr[start]<=arr[mid]): 
            start = mid+1
        elif(arr[mid]<=arr[end]):
            end = mid - 1
    return -1

def BinarySearch(arr,start,end,ele):
    while(start<=end):
        mid = start+(end-start)//2
        if arr[mid] == ele:
            return mid
        if arr[mid]<=ele:
            start = mid+1
        else:
            end = mid-1
    return -1

def FindEleInRotatedSortedArray(arr,n,ele):
    indexSmallele = RotatedArray(arr,n)
    firstHalf = BinarySearch(arr,0,indexSmallele-1,ele)
    secondHalf = BinarySearch(arr,indexSmallele,n-1,ele)
    if firstHalf != -1:
        return firstHalf
    elif secondHalf != -1:
        return secondHalf

#Driver code 
# arr = [15, 18, 2, 3, 6, 12, 13] # this is an rotated sorted array
arr = [4,5,6,7,0,1,2]
n = len(arr) 
ele = 7
print("Index of ele in rotated array ", FindEleInRotatedSortedArray(arr,n,ele))