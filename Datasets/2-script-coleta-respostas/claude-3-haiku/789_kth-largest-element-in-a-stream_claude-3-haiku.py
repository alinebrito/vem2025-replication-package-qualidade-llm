class Solution:
class KthLargest(object):
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.nums = sorted(nums, reverse=True)[:k]

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.nums) < self.k:
            self.nums.append(val)
            self.nums.sort(reverse=True)
        elif val > self.nums[-1]:
            self.nums.pop()
            self.nums.append(val)
            self.nums.sort(reverse=True)
        return self.nums[-1]