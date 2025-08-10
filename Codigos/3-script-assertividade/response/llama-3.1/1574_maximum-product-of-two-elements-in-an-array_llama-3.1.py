class Solution(object):
    def maxProduct(self, nums):
        nums.sort()
        n = len(nums)
        return max((nums[0] - 1) * (nums[n - 1] - 1), (nums[n - 1] - 1) * (nums[n - 2] - 1))