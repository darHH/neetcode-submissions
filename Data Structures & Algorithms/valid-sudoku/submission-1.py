class Solution:
    # helper to check a valid 9 grid square, given a 3x3
    def isValidSquare(self, square:List[List[str]]) -> bool:
        seen = []
        for i in range(0,3):
            for j in range(0,3):
                temp = square[i][j]
                if temp != '.':
                    if temp not in seen:
                        seen.append(temp)
                    elif temp in seen:
                        return False
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # first check if any of the 9 big squares break the rule
        for i in range(0,3):
            ix = i * 3
            for j in range(0,3):
                jx = j * 3
                temp_square = [board[ix][jx:jx+3], board[ix+1][jx:jx+3], board[ix+2][jx:jx+3]]
                if not (self.isValidSquare(temp_square)):
                    return False
        # now check global rows and cols
        seen = []
        for i in range(0,9):
            for j in range(0,9):
                temp = board[i][j]
                if temp != '.':
                    if temp in seen:
                        return False
                    else:
                        seen.append(temp)
            seen = []
        for i in range(0,9):
            for j in range(0,9):
                temp = board[j][i]
                if temp != '.':
                    if temp in seen:
                        return False
                    else:
                        seen.append(temp)
            seen = []
        return True
