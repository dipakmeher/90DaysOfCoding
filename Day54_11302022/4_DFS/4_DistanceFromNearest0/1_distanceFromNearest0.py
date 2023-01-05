def island(grid, n, m):
    global countDistance

    visited = [[False for j in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            if(grid[i][j] == "1"):
                grid[i][j] = dfs(grid, i, j, visited)
                # grid[i][j] 
    return grid
def dfs(grid, x, y, visited):
    if(x<0 or x>=len(grid) or y<0 or y>=len(grid[0]) or visited[x][y]):   
        return 10000
    if(grid[x][y] == "0"):
        return 0 
    visited[x][y] = True
    val = 1+ min(
        dfs(grid, x-1, y, visited),
        dfs(grid, x+1, y, visited),
        dfs(grid, x, y-1, visited),
        dfs(grid, x, y+1, visited)
    )
    visited[x][y] = False
    return val
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