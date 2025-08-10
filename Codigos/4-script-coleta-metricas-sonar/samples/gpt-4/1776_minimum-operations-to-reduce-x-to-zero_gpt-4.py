class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target, n = sum(nums) - x, len(nums)
        if target < 0:
            return -1
        if target == 0:
            return n
        left, max_len, current_sum = 0, -1, 0
        for right in range(n):
            current_sum += nums[right]
            while current_sum > target:
                current_sum -= nums[left]
                left += 1
            if current_sum == target:
                max_len = max(max_len, right - left + 1)
        return n - max_len if max_len != -1 else -1