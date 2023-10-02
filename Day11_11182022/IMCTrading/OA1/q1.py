import heapq

def findBestPath(n, m, startRow, startColumn, endRow, endColumn, monsterRow, monsterColumn):
    def isPathPossible(min_dist, new_x, new_y):
        for i in range(len(monsterRow)):
            if abs(new_x - monsterRow[i]) + abs(new_y - monsterColumn[i]) < min_dist:
                return False
        return True

    def bfs(min_dist):
        visited = [[False] * m for _ in range(n)]
        queue = [(startRow, startColumn)]
        visited[startRow][startColumn] = True

        while queue:
            curr_x, curr_y = queue.pop(0)
            if curr_x == endRow and curr_y == endColumn:
                return True

            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                new_x, new_y = curr_x + dx, curr_y + dy
                if 0 <= new_x < n and 0 <= new_y < m and not visited[new_x][new_y] and isPathPossible(min_dist, new_x, new_y):
                    visited[new_x][new_y] = True
                    queue.append((new_x, new_y))

        return False

    start, end = 0, n * m
    res = -1

    while start <= end:
        mid = (start + end) // 2
        if bfs(mid):
            res = mid
            start = mid + 1
        else:
            end = mid - 1

    return res


# Example usage
n = 5
m = 3
startRow = 1
startCol = 1
endRow = 4
endCol = 2
monsterRow = [0,2]
monsterCol = [2,2]

result = findBestPath(n, m, startRow, startCol, endRow, endCol, monsterRow, monsterCol)
print(result)  # Output: 3