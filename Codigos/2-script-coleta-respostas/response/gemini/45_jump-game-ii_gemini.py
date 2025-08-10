class Solution:
    def jump(self, nums):
        n, start, end, step = len(nums), 0, 0, 0
        while end < n - 1:
            step += 1
            start, end = end + 1, max(end + 1, max(i + nums[i] for i in range(start, end + 1)))
        return step