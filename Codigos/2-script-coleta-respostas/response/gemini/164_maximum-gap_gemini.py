class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2: return 0
        n = len(nums)
        min_val, max_val = min(nums), max(nums)
        if min_val == max_val: return 0
        bucket_size = (max_val - min_val) // (n - 1) or 1
        buckets = [[float('inf'), float('-inf')] for _ in range(n)]
        for num in nums:
            index = (num - min_val) // bucket_size
            buckets[index][0] = min(buckets[index][0], num)
            buckets[index][1] = max(buckets[index][1], num)
        prev_max = buckets[0][1]
        max_gap = 0
        for i in range(1, n):
            if buckets[i][0] != float('inf'):
                max_gap = max(max_gap, buckets[i][0] - prev_max)
                prev_max = buckets[i][1]
        return max_gap