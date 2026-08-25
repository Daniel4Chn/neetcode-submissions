import sys
class Solution:
    
    def solve(self, board: List[List[str]]) -> None:
        sys.setrecursionlimit(20000)

        #m x n matrix boarding contains 'X' and 'O'
        #main goal is to capture regions that are surrounded

        #conect a call is connected to adjacent cells horizontally or vertically - cells x+1, x-1, y+1, y-1
        #region: to form a region, connect every 'O' cell and they can be any shape
        #corner cells only connect to two, edge connect to three, and anything not connects to four

        #surround: a region is surrounded if none of the '0' cells in that regions are on the edge of the board so 'O' cells are on the e

        #capture a surrounded region, replace all 'O's with 'X's in place


        #a region are connected 'O' cells so maybe find the region first and then capture them with 'X's

        #possible approach is to use a set to figure out the region and then afterward replace all of them with 'X's.
        #if a O is on the edge so only 2 or 3 connected cells it can't be surrounded

        #what we should be looking at are cells that could form a region so things between 1 and len(board)-2 for x and then 1 and len(board[0])-2 for y
        if len(board) <= 2 or len(board[0]) <= 2:
            return
        visited = [[False for i in range(len(board[0]))] for j in range(len(board))]
        setOfRegionVals = set()
        safeOrNot = False
        def dfs(i, j):
            nonlocal safeOrNot
            if i < 0 or i > len(board)-1 or j < 0 or j > len(board[0])-1:
                return
            if visited[i][j] == True:
                return
            if board[i][j] == 'X':
                visited[i][j] = True
                return
            
            visited[i][j] = True

            if i == 0 or i == len(board)-1 or j == 0 or j == len(board[0])-1:
                safeOrNot = True

            setOfRegionVals.add((i, j))
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if visited[i][j] == True:
                    continue

                dfs(i, j)
                if safeOrNot == False:
                    for val in setOfRegionVals:
                        x = val[0]
                        y = val[1]
                        board[x][y] = 'X'
                setOfRegionVals = set()
                safeOrNot = False
                

        

