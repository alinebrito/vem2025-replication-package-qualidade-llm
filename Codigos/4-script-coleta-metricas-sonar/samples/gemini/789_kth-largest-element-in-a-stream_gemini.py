class Solution:
class KthLargest(object):
    def __init__(self, k, nums):
        self.k = k
        self.nums = sorted(nums)[-k:]

    def add(self, val):
        self.nums.append(val)
        self.nums = sorted(self.nums)[-self.k:]
        return self.nums[0]