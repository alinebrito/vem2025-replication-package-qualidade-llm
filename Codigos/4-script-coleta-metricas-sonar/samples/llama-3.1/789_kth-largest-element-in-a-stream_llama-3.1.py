class Solution:
    def __init__(self, k, nums):
 self.k = k
        self.nums = nums
        self.nums.sort(reverse=True)
        self.nums = self.nums[:k]

    def add(self, val):
        self.nums.append(val)
 self.nums.sort(reverse=True)
        return self.nums[self.k-1]