class Solution(object):
    def minDays(self, bloomDay, m, k):
        def canMakebouquets(days):
            bouquets, flowers = 0, 0
            for day in bloomDay:
                if day <= days:
                    flowers += 1
                    if flowers == k:
                        bouquets += 1
                        flowers = 0
                else:
                    flowers = 0
            return bouquets >= m

        left, right = 1, max(bloomDay)
        while left < right:
            mid = (left + right) // 2
            if canMakebouquets(mid):
                right = mid
            else:
                left = mid + 1
        return left if canMakebouquets(left) else -1