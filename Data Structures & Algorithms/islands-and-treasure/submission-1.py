class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #INF == can be traversed
        #-1 cant be traversed
        #0 == treasure chest
        visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]

        def bfs(grid, visited, q):
            count = 0
            while q:
                lengthOfQ = len(q)
                for i in range(lengthOfQ):
                    x,y = q.popleft()
                    if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
                        continue
                    if grid[x][y] == -1:
                        continue
                    elif visited[x][y] == True:
                        continue
                    visited[x][y] = True
                    q.append((x+1,y))
                    q.append((x-1,y))
                    q.append((x,y-1))
                    q.append((x,y+1))
                    grid[x][y] = min(grid[x][y],count)
                count+=1

        allTreasures = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    continue
                elif grid[i][j] == 0:
                    allTreasures.append([i,j])

        q = deque()
        for i in range(len(allTreasures)):
            q.append((allTreasures[i][0], allTreasures[i][1]))

        bfs(grid, visited, q)