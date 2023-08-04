import heapq
#Function
def KClosestPointsToOrigin(arr, n, k):
    #basically we have to sort using x^2+y^2
    heap = []
    # for i in range(n):
    #     heapq.heappush(heap,[-(arr[0][i]*arr[0][i]+arr[1][i]*arr[1][i]),arr[0][i],arr[1][i]])
    #     if(len(heap) > k):
    #         heapq.heappop(heap)

    for pair in arr:
        heapq.heappush(heap,[-(pair[0]*pair[0]+pair[1]*pair[1]),pair[0],pair[1]])
        if(len(heap) > k):
            heapq.heappop(heap)

    print("K closest element to Origin: ",heap)
#Driver Code
arr = [
    [1,-2], #x
    [3,2] #y
]

n = len(arr)
k = 1
KClosestPointsToOrigin(arr, n, k)