  if(x1>=0 and x1<len(grid) and y1>=0 and y1<len(grid[0]) and grid[x1][y1] == 1):
                grid[x1][y1] = "-1"
                queue.append([str(x1),str(y1)])