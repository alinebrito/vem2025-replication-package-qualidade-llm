class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10**9 + 7
        dp = [[[0] * (maxMove + 1) for _ in range(n)] for _ in range(m)]
        
        for move in range(maxMove + 1):
            for i in range(m):
                for j in range(n):
                    if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                        dp[i][j][move] = 1
                    elif move > 0:
                        dp[i][j][move] = (dp[i-1][j][move-1] + dp[i+1][j][move-1] + dp[i][j-1][move-1] + dp[i][j+1][move-1]) % MOD
        