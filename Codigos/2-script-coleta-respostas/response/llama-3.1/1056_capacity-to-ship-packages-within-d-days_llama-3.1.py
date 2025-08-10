class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        def can_ship(capacity):
            days_needed = 1
            curr_weight = 0
            for weight in weights:
                if curr_weight + weight > capacity:
                    days_needed += 1
                    curr_weight = 0
                curr_weight += weight
            return days_needed <= D

        left, right = max(weights), sum(weights)
        while left < right:
            mid = (left + right) // 2
            if can_ship(mid):
                right = mid
            else:
                left = mid + 1
        return left