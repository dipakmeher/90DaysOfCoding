#K Closest element
import heapq
#Functions
def kClosestNumbers(arr, n, k, x):
    for i in range(n):
        heapq.heappush(heap,[-abs(arr[i] - x),arr[i]])
        print(heap)
        if(len(heap) > k):
            heapq.heappop(heap)
            print(heap)
        print()
    while heap:
        res.append(heap[0][1])
        heapq.heappop(heap)
    print("k closest numbers in array is,",res)

arr = [6, 7, 9, 4, 3, 5, 8, 10, 1]
n = len(arr)
k = 3
heap = []
res = []
x = 9

kClosestNumbers(arr, n, k, x)


