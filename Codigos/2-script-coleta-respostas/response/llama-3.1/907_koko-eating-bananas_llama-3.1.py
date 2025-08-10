class Solution:
    def minEatingSpeed(self, piles, h):
        low, high = 1, 10 ** 9
        while low < high:
            mid = (low + high) // 2
            hours = sum((pile + mid - 1) // mid for pile in piles)
            if hours > h:
                low = mid + 1
            else:
                high = mid
        return low