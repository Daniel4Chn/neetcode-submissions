
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited = [[False for i in range(len(board[0]))] for j in range(len(board))]

        def dfs(i, j, visited):
            if i < 0 or i >= len(board) or j < 0 or j>= len(board[0]) or board[i][j] == 'X' or visited[i][j] == True:
                return
           
            visited[i][j] = True
            board[i][j] = 'T'
            dfs(i+1, j, visited) 
            dfs(i-1, j, visited) 
            dfs(i, j+1, visited)
            dfs(i, j-1, visited)

        boundaryCoords = []
        for i in range(len(board[0])):

            if board[0][i] == "O":
                boundaryCoords.append([0, i])
                board[0][i] = 'T'
            if board[len(board)-1][i] == "O":
                boundaryCoords.append([len(board)-1, i])
                board[len(board)-1][i] = 'T'

        for i in range(1, len(board)-1):
            if board[i][0] == "O":
                boundaryCoords.append([i, 0])
                board[i][0] = 'T'
            if board[i][len(board[0])-1] == "O":
                boundaryCoords.append([i, len(board[0])-1])
                board[i][len(board[0])-1] = 'T'

        for value in boundaryCoords:
            dfs(value[0], value[1], visited)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'T':
                    board[i][j] = 'O'




            
        