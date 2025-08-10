class Solution:
    def score(self, nums, l, r, dp):
        if dp[l][r] != -1:
            return dp[l][r]
        dp[l][r] = max(nums[l] - self.score(nums, l + 1, r, dp), nums[r] - self.score(nums, l, r - 1, dp))
        return dp[l][r]

    def PredictTheWinner(self, nums):
        n = len(nums)
        dp = [[-1] * n for _ in range(n)]
        return self.score(nums, 0, n - 1, dp) >= 0