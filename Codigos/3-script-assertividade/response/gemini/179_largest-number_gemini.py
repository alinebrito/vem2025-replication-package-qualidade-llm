class Solution:
    def largestNumber1(self, nums):
        if not any(nums):
            return "0"
        nums = map(str, nums)
        nums = sorted(nums, key=lambda x: x * 3, reverse=True)
        return str(int("".join(nums)))