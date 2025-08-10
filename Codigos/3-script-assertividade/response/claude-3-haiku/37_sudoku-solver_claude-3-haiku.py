class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        n = 9

        def is_valid(x, y, val):
            # Check row
            if val in board[x]:
                return False
            # Check column
            if val in [board[i][y] for i in range(n)]:
                return False
            # Check 3x3 sub-box
            sub_x, sub_y = x // 3, y // 3
            if val in [board[i][j] for i in range(sub_x*3, sub_x*3+3) for j in range(sub_y*3, sub_y*3+3)]:
                return False
            return True

        def solve():
            for i in range(n):
                for j in range(n):
                    if board[i][j] == '.':
                        for val in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                            if is_valid(i, j, val):
                                board[i][j] = val
                                if solve():
                                    return True
                                board[i][j] = '.'
                        return False
            return True

        solve()