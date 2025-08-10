class Solution:
    def largestNumber1(self, nums):
        if not any(nums):
            return "0"
        nums = list(map(str, nums))
        nums.sort(key=lambda x: x*10, reverse=True)
        return ''.join(nums)