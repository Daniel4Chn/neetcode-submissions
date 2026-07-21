class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        
        R = len(grid)
        C = len(grid[0])
        q = deque()
        visited = set()
        def addRoom(r,c):
            if r >= R or r < 0 or c >= C or c < 0 or (r,c) in visited or grid[r][c] == -1:
                return
            visited.add((r,c))
            q.append([r,c])

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    visited.add((r,c))
                    q.append([r,c])
        
        dist = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = dist
                addRoom(r+1,c)
                addRoom(r-1,c)
                addRoom(r,c+1)
                addRoom(r,c-1)
            dist+=1
                


    