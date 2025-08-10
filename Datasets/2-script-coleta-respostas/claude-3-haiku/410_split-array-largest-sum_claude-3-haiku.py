class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def cannot_split(max_sum, m):
            count = 1
            curr_sum = 0
            for num in nums:
                if curr_sum + num > max_sum:
                    count += 1
                    curr_sum = num
                else:
                    curr_sum += num
            return count > m

        left, right = max(nums), sum(nums)
        while left < right:
            mid = (left + right) // 2
            if cannot_split(mid, m):
                left = mid + 1
            else:
                right = mid
        return left