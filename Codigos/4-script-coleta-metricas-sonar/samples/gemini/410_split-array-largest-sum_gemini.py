class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def cannot_split(max_sum, m):
            count = 1
            current_sum = 0
            for num in nums:
                if num > max_sum:
                    return False
                current_sum += num
                if current_sum > max_sum:
                    count += 1
                    current_sum = num
            return count > m
        
        left = max(nums)
        right = sum(nums)
        while left < right:
            mid = (left + right) // 2
            if cannot_split(mid, m):
                left = mid + 1
            else:
                right = mid
        return left