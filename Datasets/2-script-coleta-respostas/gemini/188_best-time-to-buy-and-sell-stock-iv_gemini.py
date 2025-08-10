class Solution:
    def maxProfit(self, k, prices):
        n = len(prices)
        if n <= 1 or k == 0:
            return 0
        if 2 * k > n:
            profit = 0
            for i in range(1, n):
                if prices[i] > prices[i - 1]:
                    profit += prices[i] - prices[i - 1]
            return profit
        dp = [[[0 for _ in range(2)] for _ in range(k + 1)] for _ in range(n + 1)]
        for i in range(n + 1):
            for j in range(k + 1):
                dp[i][j][0] = 0
                dp[i][j][1] = -float('inf')
        for i in range(1, n + 1):
            for j in range(1, k + 1):
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i - 1])
                dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i - 1])
        return dp[n][k][0]