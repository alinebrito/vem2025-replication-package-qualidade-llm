class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        le = len(nums)
        if le < 3:
            return 0
        
        count = 0
        dp = [0] * le
        
        for i in range(2, le):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                dp[i] = dp[i-1] + 1
                count += dp[i]
        
        return count