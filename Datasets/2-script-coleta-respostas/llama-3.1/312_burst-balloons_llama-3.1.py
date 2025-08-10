class Solution:
    def maxCoins(self, nums):
        nums = [1] + [n for n in nums] + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for length in range(1, n - 1):
            for left in range(n - length - 1):
                right = left + length
                for i in range(left + 1, right):
                    dp[left][right] = max(dp[left][right], dp[left][i] + nums[left] * nums[i] * nums[right] + dp[i][right])
        return dp[0][n - 1]