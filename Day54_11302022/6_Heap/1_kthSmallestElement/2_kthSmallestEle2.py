import heapq
#Function
def kSmallestElement(arr, n, k):
    heap = []
    for i in range(n):
        heapq.heappush(heap,-arr[i])
        if(len(heap) > k):
            heapq.heappop(heap)

    print("kth smallest element is",-heap[0])
#Driver Code
arr = [6, 7, 9, 4, 3, 5, 8, 10, 1]
n = len(arr)
k = 3

kSmallestElement(arr, n, k)