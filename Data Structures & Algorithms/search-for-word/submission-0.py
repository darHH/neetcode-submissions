class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0]:
            return False
        
        rows, cols = len(board), len(board[0])

        def dfs(row, col, index):
             # all characters match
            if index == len(word):
                return True
            # out of bounds or character mismatch
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return False
            if board[row][col] != word[index]:
                return False
            
            # mark current cell as visited 
            original = board[row][col]
            board[row][col] = '#'

            is_found = (
                dfs(row + 1, col, index + 1)
                or dfs(row - 1, col, index + 1)
                or dfs(row, col + 1, index + 1)
                or dfs(row, col - 1, index + 1)
            )

            # restore for other paths
            board[row][col] = original
            return is_found

        for row in range(rows):
            for col in range(cols):
                if dfs(row, col, 0):
                    return True

        return False