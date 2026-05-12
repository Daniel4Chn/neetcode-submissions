from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        row = defaultdict(set)
        col = defaultdict(set)
        squares = defaultdict(set)

        for i in range(9):

            for j in range(9):

                r = i
                c = j
                squareID = (i//3,j//3)
                if board[r][c] == '.':
                    continue
                else:
                    if board[r][c] in row[r] or board[r][c] in col[c] or board[r][c] in squares[squareID]:
                        return False
                    else:
                        row[r].add(board[r][c])
                        col[c].add(board[r][c])
                        squares[squareID].add(board[r][c])
        return True
       