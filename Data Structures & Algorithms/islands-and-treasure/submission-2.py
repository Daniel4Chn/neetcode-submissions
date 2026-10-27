class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #INF == can be traversed
        #-1 cant be traversed
        #0 == treasure chest
        
        visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append((i,j))

      
        counter = 0
        while q:
            length = len(q)
            for i in range(length):
                value = q.popleft()
                l = value[0]
                r = value[1]
                if l < 0 or l >= len(grid) or r < 0 or r >= len(grid[0]):
                    continue
                elif visited[l][r] == True or grid[l][r] == -1:
                    continue
                visited[l][r] = True
                grid[l][r] = counter
                q.append((l+1,r))
                q.append((l-1,r))
                q.append((l,r-1))
                q.append((l,r+1))
            counter +=1
        

