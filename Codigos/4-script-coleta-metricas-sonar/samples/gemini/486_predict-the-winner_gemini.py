class Solution:
    def score(self, nums, l, r, dp):
        if dp[l][r] != -1:
            return dp[l][r]
        if l == r:
            return nums[l]
        if l + 1 == r:
            return max(nums[l], nums[r])
        dp[l][r] = max(nums[l] + min(self.score(nums, l + 2, r, dp), self.score(nums, l + 1, r - 1, dp)),
                       nums[r] + min(self.score(nums, l + 1, r - 1, dp), self.score(nums, l, r - 2, dp)))
        return dp[l][r]

    def PredictTheWinner(self, nums):
        n = len(nums)
        dp = [[-1 for _ in range(n)] for _ in range(n)]
        total = sum(nums)
        player1 = self.score(nums, 0, n - 1, dp)
        return player1 >= total - player1