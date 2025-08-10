class Solution:
    def maxCoins(self, nums):
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        for left in range(n - 2, 0, -1):
            for right in range(left, n - 1):
                for i in range(left, right + 1):
                    dp[left][right] = max(dp[left][right], nums[left - 1] * nums[i] * nums[right + 1] + dp[left][i - 1] + dp[i + 1][right])

        return dp[1][n - 2]