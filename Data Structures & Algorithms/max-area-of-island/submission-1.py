class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        visited = [[False for j in range(len(grid[0]))] for i in range(len(grid))]
        
        def dfs(visited, grid, x, y):
            nonlocal maxArea
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
                return 0
            if grid[x][y] == 0:
                return 0
            if visited[x][y] == True:
                return 0
            visited[x][y] = True
            area = 1 + dfs(visited, grid, x+1, y) + dfs(visited, grid, x-1, y) +        dfs(visited, grid, x, y+1) + dfs(visited, grid, x, y-1)
            
            maxArea = max(area, maxArea)
            return area
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                if grid[i][j] == 1 and visited[i][j] == False:
                    dfs(visited, grid, i, j)
        
        return maxArea

            

            
