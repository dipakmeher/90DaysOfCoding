#Status: Incomplete
def bfs(grid, n, m):
    queue = []
    for i in range(n):
        for j in range(m):
            if(grid[i][j] == "1"):
                queue.append([[str(i),str(j)],0])
                print(i,j)
                visited[i][j] = True

    dir = [["1","0"],["0","1"],["-1","0"],["0","-1"]]
    print(queue)
    while(len(queue)!=0):
        topEle = queue.pop(0)
        currEle = topEle[0]
        distance = topEle[1]
        dist[int(currEle[0])][int(currEle[1])] = distance
        for d in dir:
            x1 = int(currEle[0]) + int(d[0])
            y1 = int(currEle[1]) + int(d[1])

            if(x1>=0 and x1<n and y1>=0 and y1<m and visited[x1][y1]== False):
                visited[x1][y1] = True #Miskate written ==
                queue.append([[str(x1),str(y1)], distance + 1])
    return dist

#Driver Code
grid = [
  ["0","0","0"],
  ["0","1","0"],
  ["1","1","1"],
]
n = len(grid)
m = len(grid[0])
countDistance = 0
visited = [[False for j in range(m)] for i in range(n)]
dist = [[0 for j in range(m)] for i in range(n)]
print("Total no of islands are: ", bfs(grid, n, m))