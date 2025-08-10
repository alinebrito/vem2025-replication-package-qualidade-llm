class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        nums.sort()
        n = len(nums)
        res = float('inf')
        for i in range(4):
            res = min(res, nums[-1-i] - nums[i])