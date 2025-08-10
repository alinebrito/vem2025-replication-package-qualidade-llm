class Solution:
    def pivotIndex(self, nums):
        n = len(nums)
        left_sum = [0] * (n + 1)
        right_sum = [0] * (n + 1)
        
        for i in range(n):
            left_sum[i + 1] = left_sum[i] + nums[i]
            right_sum[n - i - 1] = right_sum[n - i] + nums[n - i - 1]
        
        for i in range(n):
            if left_sum[i] == right_sum[i]:
                return i
        
        return -1