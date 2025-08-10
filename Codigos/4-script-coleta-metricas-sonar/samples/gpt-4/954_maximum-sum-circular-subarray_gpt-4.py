class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        def kadane(nums):
            max_sum = curr_sum = nums[0]
            for num in nums[1:]:
                curr_sum = max(num, curr_sum + num)
                max_sum = max(max_sum, curr_sum)
            return max_sum
        
        max_kadane = kadane(A)
        total_sum = sum(A)
        min_kadane = kadane([-x for x in A])
        return max(max_kadane, total_sum + min_kadane) if total_sum != min_kadane else max_kadane