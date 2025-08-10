class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target, n = sum(nums) - x, len(nums)
        if target == 0:
            return n
        if target < 0:
            return -1
        max_len, current_sum = 0, 0
        left = 0
        for right in range(n):
            current_sum += nums[right]
            while left <= right and current_sum > target:
                current_sum -= nums[left]
                left += 1
            if current_sum == target:
                max_len = max(max_len, right - left + 1)
        return n - max_len if max_len > 0 else -1