import heapq
#Function
def frequency_Sort(arr, n):
    hashMap = dict()

    for i in arr:
        if i in hashMap:
            hashMap[i] = hashMap[i] + 1
        else:
            hashMap[i] = 1
    
    print("HashMap: ", hashMap)
    heap = []
    for key,value in hashMap.items():
        heapq.heappush(heap,[value,key]) #sort the items based on values
        
    print("Heap: ", heap)
    res = []
    while heap:
        res.append(heap[0][1])
        heapq.heappop(heap)
    print("Res: ",res)

#Driver Code
arr = [1,1,1,2,3,3,4]
n = len(arr)

frequency_Sort(arr,n)