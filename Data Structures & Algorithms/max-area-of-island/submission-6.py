class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
        maxArea = 0
        
        def dfs(i, j):
            
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return 0
            if visited[i][j] == True or grid[i][j] == 0:
                return 0
            visited[i][j] = True
            return 1+dfs(i+1,j) + dfs(i-1,j) + dfs(i,j-1) + dfs(i,j+1)
            
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    continue
                elif visited[i][j] == True:
                    continue
                value = dfs(i,j)
                maxArea = max(maxArea, value)
                
                
        
        return maxArea