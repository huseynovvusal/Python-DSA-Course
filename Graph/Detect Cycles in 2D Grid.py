from typing import List

class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m,n = len(grid), len(grid[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        visited = [[False] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if(not visited[i][j] and self.dfs(grid, directions, m, n, visited, i, j)): return True

        return False

    def dfs(self, grid, directions, m, n, visited, currX, currY, prevX = -1, prevY = -1):
        if(visited[currX][currY]): return True

        visited[currX][currY] = True

        for dX, dY in directions:
            newX, newY = currX + dX, currY + dY

            if((newX, newY) == (prevX, prevY)): continue

            if(0 <= newX < m and 0 <= newY < n and grid[currX][currY] == grid[newX][newY]):
                if(self.dfs(grid, directions, m, n, visited, newX, newY, currX, currY)):
                    return True

        return False


