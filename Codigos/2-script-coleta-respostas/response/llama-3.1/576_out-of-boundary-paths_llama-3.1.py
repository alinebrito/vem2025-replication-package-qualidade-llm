class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10**9 + 7        dp = [[[0]*maxMove + 1 for _ in range(n)] for _ in range(m)]
        for k in range(maxMove + 1):
            for i in range(m):
                for j in range(n):
                    if i == 0:
                        dp[i][j][k] += 1
                    if i == m - 1:
                        dp[i][j][k] += 1
                    if j == 0:
                        dp[i][j][k] += 1
                    if j == n - 1:
                        dp[i][j][k] += 1
                    if k > 0:
                        dp[i][j][k] += dp[max(0, i - 1)][j][k - 1]
                        dp[i][j][k] += dp[min(m - 1, i + 1)][j][k - 1]
                        dp[i][j][k] += dp[i][max(0, j - 1)][k - 1]
                        dp[i][j][k] += dp[i][min(n - 1, j + 1)][k - 1]
 dp[i][j][k] %= MOD
        return dp[startRow][startColumn][maxMove]