class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]        
        numIslands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not visited[i][j]:
                    if grid[i][j] == "0":
                        visited[i][j] = True
                        continue
                    elif grid[i][j] == "1":
                        self.DFS(grid, visited, i, j)
                        numIslands+=1
        return numIslands

    def DFS(self, grid, visited, i, j):
        if i > len(grid)-1 or i < 0 or j > len(grid[0])-1 or j < 0:
            return

        if visited[i][j] == True:
            return

        if grid[i][j] == "0":
            visited[i][j] = True
            return
        
        visited[i][j] = True
        self.DFS(grid, visited, i, j+1)
        self.DFS(grid, visited, i, j-1)
        self.DFS(grid, visited, i+1, j)
        self.DFS(grid, visited, i-1, j)

        
        
        