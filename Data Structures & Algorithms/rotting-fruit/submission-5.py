class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #first we have to figure out where the rotten fruits are
        #we have to find the location of all of the fresh fruits 
        #by the time where the rotten fruits have nowhere to spread to, we check whether there is a fresh fruit still remaining
        q = deque()
        freshFruitVars = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    freshFruitVars +=1
                elif grid[i][j] == 2:
                    q.append((i, j))
        
        minute = 0
        while q and freshFruitVars > 0:
            length = len(q)
            minute+=1
            for i in range(length):

                value = q.popleft()
                r = value[0]
                c = value[1]
                potentialValues = [[r+1, c], [r,c+1],[r-1,c],[r,c-1]]

                for combo in potentialValues:
                    l = combo[0]
                    lr = combo[1]
                    if l < 0 or l >= len(grid) or lr < 0 or lr >= len(grid[0]):
                        continue
                    if grid[l][lr] == 1:
                        grid[l][lr] = 2
                        freshFruitVars -=1
                        q.append((l,lr))

            
        if freshFruitVars == 0:
            return minute
        else:
            return -1
