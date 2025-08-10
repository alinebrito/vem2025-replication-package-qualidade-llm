class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        n = len(A)
        max_sum = float('-inf')
        min_sum = float('inf')
        curr_max = 0
        curr_min = 0
        total_sum = 0
        for num in A:
            curr_max = max(num, curr_max + num)
            max_sum = max(max_sum, curr_max)
            curr_min = min(num, curr_min + num)
            min_sum = min(min_sum, curr_min)
            total_sum += num
        return max(max_sum, total_sum - min_sum) if max_sum > 0 else max_sum