class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        n = 9

        def is_valid(num, row, col):
            for i in range(n):
                if board[row][i] == num:
                    return False
            for i in range(n):
                if board[i][col] == num:
                    return False
            start_row, start_col = row - row % 3, col - col % 3
            for i in range(3):
                for j in range(3):
                    if board[i + start_row][j + start_col] == num:
                        return False
            return True

        def solve():
            for i in range(n):
                for j in range(n):
                    if board[i][j] == '.':
                        for num in range(1, 10):
                            num = str(num)
                            if is_valid(num, i, j):
                                board[i][j] = num
                                if solve():
                                    return True
                                board[i][j] = '.'
                        return False
            return True

        solve()