# Allocate the pages in a way that each student should get atleast one book with min no of load
# Function

def isValid(arr,n,k,max):
    student = 1
    sum = 0
    for i in range(n):
        sum = sum + arr[i]
        if(sum>max):
            student+=1
            sum = arr[i]
            if(student>k):
                return False
    return True
def allocateThePages(arr, n, Range, k):
    start = 0
    end = Range
    res  = -1
    while(start<=end):
        mid = start + (end-start)//2
        if(isValid(arr,n,k,mid) == True):
            res = mid
            end = mid - 1
        else:
            start = mid+1
    return res
#Driver Code
arr = [12, 34, 67, 90]
n = len(arr)
Range = sum(arr)
k = 2
print(allocateThePages(arr, n, Range, k))