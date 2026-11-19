class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #first we have to figure out where the rotten fruits are
        #we have to find the location of all of the fresh fruits 
        #by the time where the rotten fruits have nowhere to spread to, we check whether there is a fresh fruit still remaining
        rottenFruits = []
        numOfFreshFruits = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    rottenFruits.append((i, j))
                elif grid[i][j] == 1:
                    numOfFreshFruits+=1
        if numOfFreshFruits == 0:
            return 0
        queueOfFruits = deque()
        for rottenFruit in rottenFruits:
            queueOfFruits.append(rottenFruit)
        minute = 0
        possibleChoices = [(1,0), (0,1),(-1,0),(0,-1)]
        while queueOfFruits:
            length = len(queueOfFruits)
            for i in range(length):
                rotten = queueOfFruits.popleft()
                rottenX = rotten[0]
                rottenY = rotten[1]
                for choices in possibleChoices:
                    if (rottenX+choices[0] < 0 or rottenX+choices[0] >= len(grid) or rottenY+choices[1] < 0 or rottenY+choices[1] >= len(grid[0])):
                        continue
                    elif grid[rottenX+choices[0]][rottenY+choices[1]] != 1:
                        continue
                    else:
                        queueOfFruits.append((rottenX+choices[0], rottenY+choices[1]))
                        grid[rottenX+choices[0]][rottenY+choices[1]] = 2
                        numOfFreshFruits-=1
            minute+=1
            if numOfFreshFruits == 0:
                return minute
        if numOfFreshFruits != 0:
            return -1
        else:
            return minute
        