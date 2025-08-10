class Solution:
    def __init__(self, nums):
        self.nums = nums
        self.prefix_sum = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.prefix_sum[i + 1] = self.prefix_sum[i] + nums[i]

    def update(self, index, val):
        diff = val - self.nums[index]
        self.nums[index] = val
        for i in range(index, len(self.nums)):
            self.prefix_sum[i + 1] += diff

    def sumRange(self, left, right):
 return self.prefix_sum[right + 1] - self.prefix_sum[left]