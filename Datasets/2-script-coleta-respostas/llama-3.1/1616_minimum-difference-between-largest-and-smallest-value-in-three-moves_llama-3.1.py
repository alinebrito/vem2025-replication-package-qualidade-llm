class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        res = float('inf')
        for i in range(4):
            res = min(res, nums[n - 4 + i] - nums[i])
        return res