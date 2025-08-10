class Solution:
    def check_rotation(self, nums):
        left, right = 0, len(nums) - 1
        
        while left < right:
            if nums[left] > nums[right]:
                break
            left += 1
            right -= 1
        
        return left == len(nums) or left == 0