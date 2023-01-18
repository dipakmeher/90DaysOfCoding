import heapq
#Function
def kthSmallestElement(arr, n, k):
    heap = []
    for i in range(n):
        heapq.heappush(heap,-arr[i])
        if(len(heap) > k):
            heapq.heappop(heap)

    return -heap[0]

#Driver Code
arr = [6, 7, 9, 4, 3, 5, 8, 10, 1]
n = len(arr)
k1 = 3
k2 = 6

first = kthSmallestElement(arr, n, k1)
second = kthSmallestElement(arr, n, k2)
print(first)
print(second)
Sum = 0
for i in arr:
    if(first<i and i<second): 
        Sum = Sum + i

print("Sum of elements between k1 and k2 ", Sum)