class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row pass
        seen = set()
        for row in range(9):
            for col in range(9):
                if(board[row][col] == '.'):
                    continue
                elif(board[row][col] in seen):
                    return False
                else:
                    seen.add(board[row][col])
            seen = set()

        seen = set()
        for col in range(9):
            for row in range(9):
                if(board[row][col] == '.'):
                    continue
                elif(board[row][col] in seen):
                    return False
                else:
                    seen.add(board[row][col])
            seen = set()

        seen = set()
        for square in range(9):
            for i in range(3):
                for j in range(3):
                    row = (square // 3) * 3 + i
                    # 4 // 3 = 1
                    # 1 * 1 * 3
                    col = (square % 3) * 3 + j 
                    if(board[row][col] == '.'):
                        continue
                    elif(board[row][col] in seen):
                        return False
                    else:
                        seen.add(board[row][col])
            seen = set()

        ## default
        return True
                    