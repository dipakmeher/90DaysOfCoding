import heapq
#Function
def ConnectRopesToMinCost(arr,n):
    heap = []

    for i in range(n):
        heapq.heappush(heap, arr[i])
    Sum = 0
    Cost = 0
    res = []
    while heap:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        print("a", a)
        print("b", b)
        Sum = a+b
        Cost = Sum + Cost
        print("Sum: ",Sum)
        print("======================")
        heapq.heappush(heap,Sum)
        if(len(heap) == 1): break
    Sum= Sum + b
    print(Cost)
    print(res)

    print("Min Cost to connect ropes is ",Cost)

#Driver Code
arr = [1,2,3,4,5]
n = len(arr)

ConnectRopesToMinCost(arr,n)