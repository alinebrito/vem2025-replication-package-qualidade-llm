class Solution:
class NumArray:
    def __init__(self, nums):
        self.nums = nums

    def update(self, index, val):
        self.nums[index] = val

    def sumRange(self, left, right):
        return sum(self.nums[left:right + 1])