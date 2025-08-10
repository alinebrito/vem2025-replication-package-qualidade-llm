class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = [0] * (max(nums) + 1)
        for num in nums:
            count[num] += num
        dp = [0] * (len(count) + 1)
        dp[1] = count[0]
        for i in range(2, len(count) + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + count[i - 1])
        return dp[-1]