class Solution:
    def largestNumber(self, nums):
        if not any(nums):
            return "0"
        
        nums = [str(num) for num in nums]
        nums.sort(key=lambda x: x*9, reverse=True)
        
        return ''.join(nums).lstrip('0') or "0"