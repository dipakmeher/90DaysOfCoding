def island(grid, n, m):
    global countArea
    global maxArea
    for i in range(n):
        for j in range(m):
            countArea = 0
            if(grid[i][j] == 1):
                # countArea +=1
                dfs(grid, i, j)
                maxArea = max(maxArea,countArea)
    return maxArea

def dfs(grid, x, y):
    global countArea
    if(x<0 or x>=len(grid) or y<0 or y>=len(grid[0]) or grid[x][y] == 0):
        return
    countArea+=1
    grid[x][y] = 0
    dfs(grid, x-1, y)
    dfs(grid, x+1, y)
    dfs(grid, x, y-1)
    dfs(grid, x, y+1)

#Driver Code
grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
n = len(grid)
m = len(grid[0])
maxArea = -1
countArea = 0
print("Total no of islands are: ", island(grid, n, m))