class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0

        n = len(prices)
        dp = [[0] * 2 for _ in range(n)]

        # dp[i][0] = max profit up to day i with at most one transaction
        dp[0][0] = 0
        # dp[i][1] = max profit up to day i with at most two transactions
        dp[0][1] = -prices[0]

        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])

        return dp[n - 1][0]