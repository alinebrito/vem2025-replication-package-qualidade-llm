class Solution:
    def canPartition(self, nums):
        s, n = sum(nums), len(nums)
        if s % 2 != 0:
            return False  
        target = s // 2  
        dp = [False] * (target + 1)
        dp[0] = True  
        for num in nums:
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]
        return dp[target]