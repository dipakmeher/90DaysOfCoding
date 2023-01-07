def island(grid, n, m):
    global countDistance

    visited = [[False for j in range(m)] for i in range(n)]
    dist = visited = [[-1 for j in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            if(grid[i][j] == "1"):
                grid[i][j] = bfs(grid, i, j, visited)
                # grid[i][j]
    return grid
def bfs(grid, x, y, visited):
    dir = [["1","0"],["0","1"],["-1","0"],["0","-1"]]
    queue = []
    queue.append([str(x),str(y)])
    grid[x][y] = "0"
    countArea = 0
    while(len(queue)!=0):
        currEle = queue.pop(0)
        countArea+=1
        for d in dir:
            x1 = int(currEle[0]) + int(d[0])
            y1 = int(currEle[1]) + int(d[1]) 
            if(x1>=0 and x1<len(grid) and y1>=0 and y1<len(grid[0]) and grid[x1][y1] == 1):
                grid[x1][y1] = "-1"
                queue.append([str(x1),str(y1)])
    return countArea
#Driver Code
grid = [
  ["0","0","0"],
  ["0","1","0"],
  ["1","1","1"],
]
n = len(grid)
m = len(grid[0])
countDistance = 0
print("Total no of islands are: ", island(grid, n, m))
print(countDistance)
print(grid)