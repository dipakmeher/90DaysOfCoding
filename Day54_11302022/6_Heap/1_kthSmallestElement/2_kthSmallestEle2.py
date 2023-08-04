# Kth Smallest Element using negative heapq
import heapq
#Function
def kSmallestElement(arr, n, k):
    heap = []
    for i in range(n):
        # Negative sign would store the element in decreasing order
        heapq.heappush(heap,-arr[i]) # Min heap
        if(len(heap) > k):
            #heappop would pop the first element
            heapq.heappop(heap)

    print("kth smallest element is",-heap[0])
#Driver Code
arr = [6, 7, 9, 4, 3, 5, 8, 10, 1]
n = len(arr)
k = 3

kSmallestElement(arr, n, k)