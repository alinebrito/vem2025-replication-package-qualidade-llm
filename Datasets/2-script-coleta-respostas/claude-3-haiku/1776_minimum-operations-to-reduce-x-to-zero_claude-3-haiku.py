class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target, n = sum(nums) - x, len(nums)
        if target < 0:
            return -1
        
        left, right = 0, 0
        curr_sum = 0
        max_len = -1
        
        while right < n:
            curr_sum += nums[right]
            
            while curr_sum > target:
                curr_sum -= nums[left]
                left += 1
            
            if curr_sum == target:
                max_len = max(max_len, right - left + 1)
            
            right += 1
        
        return n - max_len if max_len != -1 else -1