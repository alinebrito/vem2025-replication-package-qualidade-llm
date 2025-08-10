class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return True
        increasing = True if nums[1] >= nums[0] else False
        for i in range(2, len(nums)):
            if increasing and nums[i] < nums[i - 1]:
                return False
            if not increasing and nums[i] > nums[i - 1]:
                return False
        return True