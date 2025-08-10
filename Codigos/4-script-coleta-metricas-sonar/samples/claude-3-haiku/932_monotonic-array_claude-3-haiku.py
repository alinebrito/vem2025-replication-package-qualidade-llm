class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return True
        increasing = all(nums[i] <= nums[i+1] for i in range(len(nums)-1))
        decreasing = all(nums[i] >= nums[i+1] for i in range(len(nums)-1))
        return increasing or decreasing