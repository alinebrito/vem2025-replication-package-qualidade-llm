class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def cannot_split(max_sum, m):
            count, current_sum = 1, 0
            for num in nums:
                current_sum += num
                if current_sum > max_sum:
                    count += 1
                    current_sum = num
            return count > m

        left, right = max(nums), sum(nums)
        while left < right:
            mid = (left + right) // 2
            if cannot_split(mid, k):
                left = mid + 1
            else:
                right = mid
        return left