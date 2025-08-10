class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        n = len(A)
        max_sum = float('-inf')
        min_sum = float('inf')
        total_sum = 0
        curr_max_sum = 0
        curr_min_sum = 0
        
        for num in A:
 total_sum += num
            curr_max_sum = max(num, curr_max_sum + num)
            max_sum = max(max_sum, curr_max_sum)
            curr_min_sum = min(num, curr_min_sum + num)
            min_sum = min(min_sum, curr_min_sum)
        
        if max_sum > 0:
            return max(max_sum, total_sum - min_sum)
        else:
            return max_sum