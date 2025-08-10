class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        target, n = sum(nums) - x, len(nums)
        if target < 0:
            return -1
        
        left, right, curr_sum, min_op = 0, 0, 0, float('inf')
        while right < n:
            curr_sum += nums[right]
            while curr_sum > target:
                curr_sum -= nums[left]
                left += 1
            if curr_sum == target:
                min_op = min(min_op, left + n - right -1)
            right += 1
        return min_op if min_op != float('inf') else -1
