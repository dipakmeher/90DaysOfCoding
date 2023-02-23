import heapq
def interviewOne(input, n):
    hashMap = dict()
    for rec in input:
        if rec[1] in hashMap:
            hashMap[rec[1]] += rec[2]
        else:
            hashMap[rec[1]] = rec[2]
    
    print(hashMap)

    heap = []
    for key,val in hashMap.items():
        heapq.heappush(heap, [val, key])
        if(len(heap) > n):
            heapq.heappop(heap)
    print(heap)
    res = []
    for i in range(len(heap)-1, -1, -1): # Error 
        res.append(heap[i][1]) # Error
    print(res)


#Driver Code
input = [("10:00","John",1), ("10:20","Maria",2), ("10:30","John",5)]
n = 2 # num of elements to be returned
interviewOne(input, n)