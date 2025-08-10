class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        longest = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                subarray = nums[i:j+1]
                if all(abs(x - y) <= limit for x in subarray for y in subarray):
                    longest = max(longest, len(subarray))
        return longest