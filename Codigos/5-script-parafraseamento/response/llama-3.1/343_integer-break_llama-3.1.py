class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [None, 1]
        for i in range(2, n + 1):
            max_val = 0
            for j in range(1, i // 2 + 1):
                max_val = max(max_val, max(j * (i - j), j * dp[i - j]))
            dp.append(max_val)
        return dp[n]