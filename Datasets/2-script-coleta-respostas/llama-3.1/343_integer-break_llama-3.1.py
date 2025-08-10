class Solution:
    def integerBreak(self, n):
        dp = [None, 1]
        for i in range(2, n + 1):
            max_product = 0
            for j in range(1, i):
                product = j * (i - j) * dp[i - j]
                max_product = max(max_product, product)
            dp.append(max_product)
        return dp[n]