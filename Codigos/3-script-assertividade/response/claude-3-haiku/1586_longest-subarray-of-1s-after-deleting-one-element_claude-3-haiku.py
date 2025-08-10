class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left, right, max_len, zeros = 0, 0, 0, 0
        while right < len(nums):
            if nums[right] == 0:
                zeros += 1
            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            max_len = max(max_len, right - left)
            right += 1
        return max_len