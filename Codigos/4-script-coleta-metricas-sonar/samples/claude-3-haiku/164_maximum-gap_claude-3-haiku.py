class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0

        max_num = max(nums)
        min_num = min(nums)
        bucket_size = max(1, (max_num - min_num) // (len(nums) - 1))
        bucket_num = (max_num - min_num) // bucket_size + 1

        buckets = [[float('inf'), float('-inf')] for _ in range(bucket_num)]

        for num in nums:
            index = (num - min_num) // bucket_size
            buckets[index][0] = min(buckets[index][0], num)
            buckets[index][1] = max(buckets[index][1], num)

        prev_max = min_num
        max_gap = 0
        for bucket in buckets:
            if bucket[0] == float('inf') and bucket[1] == float('-inf'):
                continue
            max_gap = max(max_gap, bucket[0] - prev_max)
            prev_max = bucket[1]

        return max_gap