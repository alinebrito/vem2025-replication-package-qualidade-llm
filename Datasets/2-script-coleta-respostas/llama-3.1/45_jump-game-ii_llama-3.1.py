class Solution:
    def jump(self, nums):
        n, start, end, step = len(nums), 0, 0, 0
        while end < n - 1:
            step += 1
            max_reach = end
            for i in range(start, end + 1):
                max_reach = max(max_reach, i + nums[i])
            start = end + 1
            end = max_reach
        return step
