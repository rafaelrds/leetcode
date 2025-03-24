from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        def is_valid(i, j, grid):
            in_rows = 0 <= i < len(grid)
            in_columns = 0 <= j < len(grid[0])
            return in_rows and in_columns

        def is_land(i, j, grid):
            return grid[i][j] == "1"

        def dfs(i, j, grid):
            if not is_valid(i, j, grid) or not is_land(i, j, grid):
                return

            grid[i][j] = "0"
            dfs(i+1, j, grid)
            dfs(i-1, j, grid)
            dfs(i, j+1, grid)
            dfs(i, j-1, grid)

        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i, j, grid) # sink all lands connected to this land
                    islands += 1
        return islands
