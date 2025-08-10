class Solution:
    def splitArray(self, nums, m):
        def cannot_split(max_sum, m):
            left, right = max(nums), sum(nums)
            while left < right:
                mid = (left + right) // 2
                if self.can_split(nums, mid, m):
                    right = mid
                else:
                    left = mid + 1
            return left

        def can_split(nums, max_sum, m):
            count, current_sum = 1, 0
            for num in nums:
                if current_sum + num > max_sum:
                    count += 1
                    current_sum = num
                else:
                    current_sum += num
            return count <= m

        return cannot_split(max(nums), m)