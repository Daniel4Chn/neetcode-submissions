class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
        maxArea = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not visited[i][j]:
                    if grid[i][j] == 0:
                        visited[i][j] = True
                        continue
                    elif grid[i][j] == 1:
                        maxValue = self.DFS(visited, grid, i, j)
                        maxArea = max(maxArea, maxValue)
        return maxArea

    def DFS(self, visited, grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
            return 0
        if visited[i][j] == True:
            return 0
        elif grid[i][j] == 0:
            visited[i][j] = True
            return 0
        elif grid[i][j] == 1:
            visited[i][j] = True
            v1 = self.DFS(visited, grid, i+1, j)
            v2 = self.DFS(visited, grid, i-1, j)
            v3 = self.DFS( visited, grid, i, j-1)
            v4 = self.DFS(visited, grid, i, j+1)
            return 1 + v1 + v2 + v3 + v4