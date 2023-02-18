# Sort the kSortedArray or Nearly sorted array
# k tells that the element is present within k range left or right

import heapq
#Function
def sortKSortedArray(arr,n,k):
    heap = arr[:k+1]
    heapq.heapify(heap)

    index = 0
    for remEle in range(k+1,n):
        arr[index] = heapq.heappop(heap)
        heapq.heappush(heap,arr[remEle])
        index+=1
    
    while heap:
        arr[index] = heapq.heappop(heap)
        index+=1

    print(arr)

#Drive Code
k = 4
arr = [6,5,3,2,8,10,9]
n = len(arr)
print(arr)
sortKSortedArray(arr,n,k)