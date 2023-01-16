# Get the k frequent numbers in array
import heapq
#Functions
def kFrequentNumbers(arr,n,k):
    hashMap = dict()

    for i in arr:
        if i in hashMap:
            hashMap[i] = hashMap[i] + 1
        else:
            hashMap[i] = 1
    
    heap = []
    for key,value in hashMap.items():
        heapq.heappush(heap,[value,key])
        if(len(heap) > k):
            heapq.heappop(heap) # small elements will popped
    
    print(heap)
    res = []
    while heap:
        res.append(heap[0][1]) # Since all the ele in heap are answers, we can append in this way
        heapq.heappop(heap)
    print("Most frequent k elements in array are,", res)

#Driver Code
arr = [1,1,1,3,2,2,4]
n = len(arr)
k=2
kFrequentNumbers(arr,n,k)