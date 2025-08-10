class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        def canShip(capacity):
            days_needed = 1
            current_weight = 0
            for weight in weights:
                if current_weight + weight > capacity:
                    days_needed += 1
                    current_weight = weight
                    if days_needed > D:
                        return False
                else:
                    current_weight += weight
            return True

        left, right = max(weights), sum(weights)
        while left < right:
            mid = (left + right) // 2
            if canShip(mid):
                right = mid
            else:
                left = mid + 1
        return left