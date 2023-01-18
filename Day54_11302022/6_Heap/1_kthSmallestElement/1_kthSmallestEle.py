#Find the kth smallest element in heap
import heapq

#Driver Code
arr = [6, 7, 9, 4, 3, 5, 8, 10, 1]
k = 3
heapq.heapify(arr)

print(heapq.nsmallest(k,arr))

print(heapq.nsmallest(k,arr)[-1])

