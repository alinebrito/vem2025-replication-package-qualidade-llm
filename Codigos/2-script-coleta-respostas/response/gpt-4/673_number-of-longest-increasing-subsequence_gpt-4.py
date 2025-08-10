class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        lengths = [1] * n
        counts = [1] * n
        max_length = 0
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if lengths[j] + 1 > lengths[i]:
                        lengths[i] = lengths[j] + 1
                        counts[i] = counts[j]
                    elif lengths[j] + 1 == lengths[i]:
                        counts[i] += counts[j]
        max_length = max(lengths)
        return sum(c for l, c in zip(lengths, counts) if l == max_length)