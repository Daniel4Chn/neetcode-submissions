class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        visitedArr = [[False for i in range(len(grid[0]))] for j in range(len(grid))]

        numOfIslands = 0
        def dfs(x,y):

            if x < 0 or x >= len(grid) or y < 0 or y>= len(grid[0]):
                return
            if visitedArr[x][y] == True:
                return
            elif grid[x][y] == '0':
                visitedArr[x][y] = True
                return
            visitedArr[x][y] = True
            dfs(x+1,y)
            dfs(x-1,y)
            dfs(x,y+1)
            dfs(x,y-1)
            

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if visitedArr[i][j] == True:
                    continue
                elif grid[i][j] == '0':
                    visitedArr[i][j] = True
                    continue
                dfs(i,j)
                numOfIslands+=1
        
        return numOfIslands
        
                