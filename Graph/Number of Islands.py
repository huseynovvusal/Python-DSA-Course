from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        res = 0

        for i in range(m):
            for j in range(n):
                if(grid[i][j] == "1"):
                    self.dfs(grid,directions,i,j,m,n)
                    res += 1

        return res


    def dfs(self, grid, directions, x, y, m, n):
        grid[x][y] = "0"

        for xi,yi in directions:
            newX,newY = x + xi, y + yi

            if(0 <= newX < m and 0 <= newY < n and grid[newX][newY] == "1"):
                self.dfs(grid, directions, newX, newY, m, n)





