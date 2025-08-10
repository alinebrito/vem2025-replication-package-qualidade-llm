class Solution:
    def score(self, nums, l, r, dp):
        if dp[l][r] != -1:

            n = len(nums)
            prefixSum = [0] * (n + 1)

            for i in range(n):
                prefixSum[i+1] = prefixSum[i] + nums[i]

            dp = [[-1] * n for _ in range(n)]

            for i in range(n):
                dp[i][i] = nums[i]

            for gap in range(1, n):
                for i in range(n - gap):
                    j = i + gap
                    dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1])

            return dp[0][-1] >= 0