class Solution:
    def numDistinct(self, s, t):
        dp = [[0] * (len(s) + 1) for _ in range(len(t) + 1)]
        for col in range(len(s) + 1):
            dp[0][col] = 1
        for row in range(1, len(t) + 1):
            for col in range(1, len(s) + 1):
                if t[row - 1] == s[col - 1]:
                    dp[row][col] = dp[row - 1][col - 1] + dp[row][col - 1]
                else:
                    dp[row][col] = dp[row][col - 1]
        return dp[-1][-1]