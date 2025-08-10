class Solution(object):
    def minDays(self, bloomDay, m, k):
        if m * k > len(bloomDay):
            return -1
        left, right = 1, max(bloomDay)
        
        def canMakeBouquets(day):
            count, bouquets = 0, 0
            for bloom in bloomDay:
                if bloom <= day:
                    count += 1
                    if count == k:
                        bouquets += 1
                        count = 0
                else:
                    count = 0
            return bouquets >= m
        
        while left < right:
            mid = (left + right) // 2
            if canMakeBouquets(mid):
                right = mid
            else:
                left = mid + 1
        return left