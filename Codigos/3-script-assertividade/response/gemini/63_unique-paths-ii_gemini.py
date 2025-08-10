class Solution:
    def uniquePathsWithObstacles1(self, obstacleGrid):
        if not obstacleGrid:
            return 
        r, c = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in range(c)] for _ in range(r)]
        dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 0
        for i in range(1, r):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = dp[i - 1][0]
        for j in range(1, c):
            if obstacleGrid[0][j] == 0:
                dp[0][j] = dp[0][j - 1]
        for i in range(1, r):
            for j in range(1, c):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]