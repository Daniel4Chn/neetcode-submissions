class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(len(board)):
            numbersInRow = set()
            for j in range(len(board[i])):
                if board[i][j] == ".": 
                    continue
                if board[i][j] in numbersInRow:
                    return False
                else:
                    numbersInRow.add(board[i][j])
        
        for i in range(len(board[0])):
            numbersInColumn = set()
            for j in range(len(board)):
                if board[j][i] == ".": 
                    continue
                if board[j][i] in numbersInColumn:
                    return False
                else:
                    numbersInColumn.add(board[j][i])
        
        for i in range(9):
            numbersInSquare = set() #i//3-> 0 and j//3 -> 0
            for j in range((i//3)*3,(i//3)*3+3):
                for k in range(i%3*3,i%3*3+3):
                    if board[j][k] == ".": 
                        continue
                    if board[j][k] in numbersInSquare:
                        return False
                    else:
                        numbersInSquare.add(board[j][k])
                
        return True