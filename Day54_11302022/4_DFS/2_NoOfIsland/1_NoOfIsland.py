def island(grid, n, m):
    countIsland = 0
    for i in range(n):
        for j in range(m):
            if(grid[i][j] == "1"):
                countIsland +=1
                dfs(grid, i, j)
    return countIsland

def dfs(grid, x, y):
    if(x<0 or x>=len(grid) or y<0 or y>=len(grid[0]) or grid[x][y] == "0"):
        return
    grid[x][y] = "0"
    dfs(grid, x-1, y)
    dfs(grid, x+1, y)
    dfs(grid, x, y-1)
    dfs(grid, x, y+1)

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
n = len(grid)
m = len(grid[0])

print("Total no of islands are: ", island(grid, n, m))