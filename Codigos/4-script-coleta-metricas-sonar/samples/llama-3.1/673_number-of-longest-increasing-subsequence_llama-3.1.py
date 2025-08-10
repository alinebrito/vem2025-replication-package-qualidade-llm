class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0

        n = len(nums)
        lengths = [1] * n
        counts = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if lengths[i] == lengths[j]:
                        lengths[i] = lengths[j] + 1
                        counts[i] = counts[j]
                    elif lengths[i] == lengths[j] + 1:
                        counts[i] += counts[j]

        max_length = max(lengths)
        return sum(count for length, count in zip(lengths, counts) if length == max_length)