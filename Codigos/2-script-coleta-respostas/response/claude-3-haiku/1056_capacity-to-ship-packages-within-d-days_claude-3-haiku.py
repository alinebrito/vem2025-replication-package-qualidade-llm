class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        left, right = max(weights), sum(weights)
        while left < right:
            mid = (left + right) // 2
            if self.canShipWithinDays(weights, D, mid):
                right = mid
            else:
                left = mid + 1
        return left

    def canShipWithinDays(self, weights: List[int], D: int, capacity: int) -> bool:
        days, total = 1, 0
        for weight in weights:
            if total + weight > capacity:
                days += 1
                total = weight
            else:
                total += weight
        return days <= D