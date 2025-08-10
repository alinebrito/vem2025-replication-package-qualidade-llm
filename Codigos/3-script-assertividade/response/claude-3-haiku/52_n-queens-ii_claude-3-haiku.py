class Solution:
    def totalNQueens(self, n):
        self.res = 0
        self.backtrack(n, [])
        return self.res

    def backtrack(self, n, queens):
        row = len(queens)
        if row == n:
            self.res += 1
            return
        for col in range(n):
            if self.is_safe(queens, row, col):
                queens.append(col)
                self.backtrack(n, queens)
                queens.pop()

    def is_safe(self, queens, row, col):
        for r, c in enumerate(queens):
            if c == col or abs(row - r) == abs(col - c):
                return False
        return True