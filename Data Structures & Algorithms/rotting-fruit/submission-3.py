class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fruits = False
  
        visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
        arrOfRotton = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    arrOfRotton.append([i,j])
                elif grid[i][j] == 1:
                    fruits = True
        if fruits and len(arrOfRotton) == 0:
            return -1
        elif not fruits and len(arrOfRotton) == 0:
            return 0
        
        minute = -1
        q = deque()
        
        for i in range(len(arrOfRotton)):
            q.append(arrOfRotton[i])
        
        while q:
            lengthOfQ = len(q)
            for i in range(lengthOfQ):
                x,y = q.popleft()
                if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
                    continue
                elif grid[x][y] == 0:
                    continue
                elif visited[x][y] == True:
                    continue
                visited[x][y] = True
                q.append([x+1,y])
                q.append([x-1,y])
                q.append([x,y+1])
                q.append([x,y-1])
                grid[x][y] = 2
            if q:
                minute+=1
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        return minute