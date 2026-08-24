class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        def bfs(heights, i, j):
            visited = set()
            q = deque()
            q.append([i, j])
            reachPacific = False
            reachAtlantic = False
            while q:
                leng = len(q)
                for elem in range(leng):
                    x, y = q.popleft()
                    if (x, y) in visited:
                        continue
                    visited.add((x,y))
                    if x<0 or x>=len(heights) or y < 0 or y >= len(heights[0]):
                        if x < 0:
                            reachPacific = True
                            
                        elif x >= len(heights):
                            reachAtlantic = True
                            
                        if y < 0:
                            reachPacific = True
                            
                        elif y >= len(heights[0]):
                            reachAtlantic = True
                        continue

                    if x != len(heights)-1:
                        if heights[x+1][y] <= heights[x][y]:
                            q.append([x+1, y])
                    else:
                        q.append([x+1, y])

                    if x != 0:
                        if heights[x-1][y] <= heights[x][y]:
                            q.append([x-1, y])
                    else:
                        q.append([x-1, y])

                    if y != len(heights[0])-1:
                        if heights[x][y+1] <= heights[x][y]:
                            q.append([x, y+1])
                    else:
                        q.append([x, y+1])
                    if y!= 0:
                        if heights[x][y-1] <= heights[x][y]:
                            q.append([x, y-1])
                    else:
                        q.append([x, y-1])
                    
            
            if reachPacific and reachAtlantic:
                return True
            else:
                return False
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                value = bfs(heights, i, j)
                
                if value == True:
                    res.append([i,j])

        return res

        # if x == -1 that means pacific
        # if x == len(heights) that means atlantic
        # if y == -1 that means pacific
        # if y == len(heights) that means atlantic
