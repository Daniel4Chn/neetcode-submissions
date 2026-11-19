class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        visitedArr = [[False for i in range(len(grid[0]))] for j in range(len(grid))]

        def dfs(grid, i, j, visitedArr):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return
            if visitedArr[i][j] == True or grid[i][j] == '0':
                return
            
            visitedArr[i][j] = True
            dfs(grid, i-1, j, visitedArr)
            dfs(grid, i+1,j, visitedArr)
            dfs(grid, i, j+1, visitedArr)
            dfs(grid, i, j-1, visitedArr)

        
        numberOfIslands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if visitedArr[i][j] == True:
                    continue
                if grid[i][j] == '1':
                    dfs(grid, i, j, visitedArr)
                    numberOfIslands+=1

        
        return numberOfIslands