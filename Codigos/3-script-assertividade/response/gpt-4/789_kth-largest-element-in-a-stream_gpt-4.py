class Solution:
    class KthLargest(object):
        def __init__(self, k, nums):
            self.k = k  
            self.nums = sorted(nums)
        
        def add(self, val):
            from bisect import insort  
            insort(self.nums, val)
            return self.nums[-self.k]