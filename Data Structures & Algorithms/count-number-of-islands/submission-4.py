class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
        numOfIslands = 0
        def dfs(i, j):
            nonlocal numOfIslands
            if i < 0 or i >= len(grid) or j < 0 or j>=len(grid[0]):
                return
            elif grid[i][j] == '0' or visited[i][j] == True:
                return
            visited[i][j] = True
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
            

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if visited[i][j] == True:
                    continue
                elif grid[i][j] == '0':
                    continue
                dfs(i, j)
                numOfIslands+=1
        return numOfIslands
                
                