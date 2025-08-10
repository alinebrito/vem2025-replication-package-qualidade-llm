class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0
        n = len(prices)
        dp = [[[0 for _ in range(2)] for _ in range(3)] for _ in range(n)]
        for i in range(n):
            for k in range(1, 3):
                dp[i][k][0] = float('-inf')
        for i in range(n):
            for k in range(1, 3):
                dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k - 1][1] + prices[i])
                dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k][0] - prices[i])
        return dp[n - 1][2][0]