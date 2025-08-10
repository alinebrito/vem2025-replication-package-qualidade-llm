class Solution:
    def totalNQueens(self, n):
        self.res = 0  
        self.solve(n, 0, [], set(), set(), set())
        return self.res
    
    def solve(self, n, row, cols, diag1, diag2):
        if row == n:
            self.res += 1  
            return  
        for col in range(n):
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue  
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)
            self.solve(n, row + 1, cols, diag1, diag2)
            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)