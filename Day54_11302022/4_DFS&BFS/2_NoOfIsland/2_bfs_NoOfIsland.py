def island(grid, n, m):
    countIsland = 0
    for i in range(n):
        for j in range(m):
            if(grid[i][j] == "1"):
                countIsland +=1
                bfs(grid, i, j)
    return countIsland

def bfs(grid, x, y):
    dir = [["1","0"],["0","1"],["-1","0"],["0","-1"]]
    queue = []
    queue.append([str(x),str(y)])
    grid[x][y] = "0"

    while(len(queue)!=0):
        currEle = queue.pop(0)
        for d in dir:
            x1 = int(currEle[0]) + int(d[0])
            y1 = int(currEle[1]) + int(d[1])

            if(x1<0 or x1>=len(grid) or y1<0 or y1>=len(grid[0]) or grid[x1][y1] == "0"):
                continue
            grid[x1][y1] = "0"
            queue.append([str(x1),str(y1)])

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","1"]
]
n = len(grid)
m = len(grid[0])

print("Total no of islands are: ", island(grid, n, m))