class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        row=[set() for _ in range(9)]
        col=[set() for _ in range(9)]
        squar=[set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                b=(i//3)*3+(j//3)
                if board[i][j]==".":
                    continue
                elif board[i][j] not in row[i] and board[i][j] not in col[j] and board[i][j] not in squar[b]:
                    row[i].add(board[i][j])
                    col[j].add(board[i][j])
                    squar[b].add(board[i][j])
                else: 
                    return False
        return True