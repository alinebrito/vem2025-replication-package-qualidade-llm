class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        f = 1
        if len(nums) < 2:
            return len(nums)
        diff = nums[1] - nums[0]
        if diff != 0:
            f = 2
        for i in range(2, len(nums)):
            if (diff > 0 and nums[i] - nums[i - 1] < 0) or (diff < 0 and nums[i] - nums[i - 1] > 0):
                f += 1
                diff = nums[i] - nums[i - 1]
        return f