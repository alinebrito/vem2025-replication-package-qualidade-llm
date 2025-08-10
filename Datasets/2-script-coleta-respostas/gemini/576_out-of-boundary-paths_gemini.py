class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        dp = [[[-1 for _ in range(maxMove + 1)] for _ in range(n)] for _ in range(m)]
        mod = 10**9 + 7
        
        def solve(row, col, moves):
            if row < 0 or col < 0 or row == m or col == n:
                return 1
            if moves == 0:
                return 0
            if dp[row][col][moves] != -1:
                return dp[row][col][moves]
            
            left = solve(row, col - 1, moves - 1) % mod
            right = solve(row, col + 1, moves - 1) % mod
            up = solve(row - 1, col, moves - 1) % mod
            down = solve(row + 1, col, moves - 1) % mod
            
            dp[row][col][moves] = (left + right + up + down) % mod
            return dp[row][col][moves]
        
        return solve(startRow, startColumn, maxMove)