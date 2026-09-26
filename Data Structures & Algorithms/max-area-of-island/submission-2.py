class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visitedArr = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
       
        maxArea = 0

        def dfs(i,j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return 0
            
            if visitedArr[i][j] == True:
                return 0
            elif grid[i][j] == 0:
                return 0
            
            visitedArr[i][j] = True
            value = dfs(i+1,j)
            value2 = dfs(i-1,j)
            value3 = dfs(i,j+1)
            value4 = dfs(i,j-1)
            return 1+value+value2+value3+value4

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if visitedArr[i][j] == True:
                    continue
                elif grid[i][j] == '0':
                    visitedArr[i][j] = True
                    continue
                
                area = dfs(i,j)
                print(area)
                maxArea = max(area,maxArea)
        
        return maxArea