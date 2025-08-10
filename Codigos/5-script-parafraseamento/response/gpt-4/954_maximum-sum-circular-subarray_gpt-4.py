class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        total = sum(A)
        max_ending_here = max_so_far = A[0]
        min_ending_here = min_so_far = A[0]
        
        for i in range(1, len(A)):
            max_ending_here = max(A[i], max_ending_here + A[i])
            max_so_far = max(max_so_far, max_ending_here)
            min_ending_here = min(A[i], min_ending_here + A[i])
            min_so_far = min(min_so_far, min_ending_here)
        
        if max_so_far > 0:
            return max(max_so_far, total - min_so_far)
        return max_so_far  