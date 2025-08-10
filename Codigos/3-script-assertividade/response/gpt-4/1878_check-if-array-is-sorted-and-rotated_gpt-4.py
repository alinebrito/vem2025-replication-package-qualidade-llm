class Solution:
    def check_rotation(self, nums):
        left, right = 0, len(nums) - 1  
        while left < right and nums[left] == nums[right]:
            right -= 1  
        count = 0  
        while left < right:
            if nums[left] > nums[left + 1]:
                count += 1  
            left += 1  
        return count <= 1  