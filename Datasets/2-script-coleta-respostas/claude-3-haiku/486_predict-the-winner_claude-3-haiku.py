class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [[-1] * n for _ in range(n)]

        def score(self, nums, l, r, dp):
            if dp[l][r] != -1:
                return dp[l][r]
            if l == r:
                return nums[l]
            dp[l][r] = max(nums[l] - score(self, nums, l + 1, r, dp), nums[r] - score(self, nums, l, r - 1, dp))
            return dp[l][r]

        return score(self, nums, 0, n - 1, dp) >= 0