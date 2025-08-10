class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        left, right = max(weights), sum(weights)
        while left <= right:
            mid = (left + right) // 2
            if self.canShip(weights, D, mid):
                right = mid - 1
            else:
                left = mid + 1
        return left

    def canShip(self, weights: List[int], D: int, capacity: int) -> bool:
        days = 1
        current_weight = 0
        for weight in weights:
            if current_weight + weight > capacity:
                days += 1
                current_weight = 0
            current_weight += weight
        return days <= D