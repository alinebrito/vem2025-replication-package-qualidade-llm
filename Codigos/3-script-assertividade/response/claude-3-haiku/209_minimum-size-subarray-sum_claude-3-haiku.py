class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, total, res = 0, 0, float('inf')
        for right in range(len(nums)):
            total += nums[right]
            while total >= target:
                res = min(res, right - left + 1)
                total -= nums[left]
                left += 1
        return 0 if res == float('inf') else res