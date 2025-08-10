class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]

        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0

        dp[0][0] = 1

        for i in range(1, m):
            dp[i][0] = 1 if obstacleGrid[i][0] == 0 and dp[i-1][0] else 0

        for j in range(1, n):
            dp[0][j] = 1 if obstacleGrid[0][j] == 0 and dp[0][j-1] else 0

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1] if obstacleGrid[i][j] == 0 else 0

        return dp[m-1][n-1]