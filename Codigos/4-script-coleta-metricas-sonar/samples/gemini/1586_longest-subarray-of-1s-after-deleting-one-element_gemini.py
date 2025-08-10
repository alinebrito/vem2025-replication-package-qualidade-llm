class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return n - 1
        left = [0] * n
        right = [0] * n
        count = 0
        for i in range(n):
            if nums[i] == 1:
                count += 1
            else:
                count = 0
            left[i] = count
        count = 0
        for i in range(n - 1, -1, -1):
            if nums[i] == 1:
                count += 1
            else:
                count = 0
            right[i] = count
        max_len = 0
        for i in range(n):
            if i == 0:
                max_len = max(max_len, right[i + 1])
            elif i == n - 1:
                max_len = max(max_len, left[i - 1])
            else:
                max_len = max(max_len, left[i - 1] + right[i + 1])
        return max_len