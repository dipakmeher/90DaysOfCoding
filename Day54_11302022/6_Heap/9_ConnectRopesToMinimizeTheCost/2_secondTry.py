import heapq
#Function
def ConnectRopesToMinCost(arr,n):
    heap = []

    for i in range(n):
        heapq.heappush(heap, arr[i])
    Sum = 0
    res = []
    while heap:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        print("a", a)
        print("b", b)
        Sum = a+b
        print("Sum: ",Sum)
        print("======================")
        res.append(Sum)
        heapq.heappush(heap,Sum)
        if(len(heap) == 1): break
    print(res)

    print("Min Cost to connect ropes is ",Sum(res))

#Driver Code
arr = [1,2,3,4,5]
n = len(arr)

ConnectRopesToMinCost(arr,n)