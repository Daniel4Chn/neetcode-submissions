class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
        numberOfIslands = 0

        def dfs(grid, visited, i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return
            if visited[i][j] or grid[i][j] == '0':
                return
            visited[i][j] = True
            dfs(grid, visited, i+1, j)
            dfs(grid, visited, i-1, j)
            dfs(grid, visited, i, j-1)
            dfs(grid, visited, i, j+1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and not visited[i][j]:
                    dfs(grid, visited, i, j)
                    numberOfIslands += 1
        return numberOfIslands