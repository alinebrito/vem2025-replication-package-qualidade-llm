class Solution:
    def largestNumber1(self, nums):
        if not any(nums):
            return "0"
        nums = sorted(map(str, nums), key=lambda x: x*10, reverse=True)
        return ''.join(nums)