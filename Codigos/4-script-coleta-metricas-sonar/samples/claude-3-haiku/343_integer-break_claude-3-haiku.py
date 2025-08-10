class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [None, 1]
        for i in range(2, n+1):
            max_product = 0
            for j in range(1, i//2+1):
                max_product = max(max_product, j * (i-j), j * dp[i-j])
            dp.append(max_product)
        return dp[n]