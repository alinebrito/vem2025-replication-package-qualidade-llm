class Solution:
    def exist(self, board, word):
        rows, cols = len(board), len(board[0])

        def backtrack(row, col, i):
            if i == len(word):
                return True

            if 0 <= row < rows and 0 <= col < cols and board[row][col] == word[i]:
                board[row][col] = '#'  # mark visited cell

                found = backtrack(row + 1, col, i + 1) or \
                       backtrack(row - 1, col, i + 1) or \
                       backtrack(row, col + 1, i + 1) or \
                       backtrack(row, col - 1, i + 1)

                board[row][col] = word[i]  # backtrack (unmark)

                return found
            return False

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0] and backtrack(row, col, 1):
                    return True

        return False