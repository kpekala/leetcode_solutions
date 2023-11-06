from typing import List


class Solution:

    def dfs(self, grid, i, j):
        m = len(grid)
        n = len(grid[0])
        grid[i][j] = '2'
        if i + 1 < m and grid[i+1][j] == '1':
            self.dfs(grid, i+1, j)
        if j + 1 < n and grid[i][j+1] == '1':
            self.dfs(grid, i, j+1)
        if i - 1 >= 0 and grid[i-1][j] == '1':
            self.dfs(grid, i-1, j)
        if j - 1 >= 0 and grid[i][j-1] == '1':
            self.dfs(grid, i, j-1)

    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    self.dfs(grid, i, j)

        return res

sol = Solution()

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

print(sol.numIslands(grid))

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

print(sol.numIslands(grid))

