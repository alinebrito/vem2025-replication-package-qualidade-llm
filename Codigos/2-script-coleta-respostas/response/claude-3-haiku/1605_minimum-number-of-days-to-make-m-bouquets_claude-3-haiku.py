class Solution(object):
    def minDays(self, bloomDay, m, k):
        n = len(bloomDay)
        if m * k > n:
            return -1
        
        left, right = min(bloomDay), max(bloomDay)
        while left <= right:
            mid = (left + right) // 2
            if self.canMakeBouquets(bloomDay, m, k, mid):
                right = mid - 1
            else:
                left = mid + 1
        return left
    
    def canMakeBouquets(self, bloomDay, m, k, days):
        bouquets, flowers = 0, 0
        for bloom in bloomDay:
            if bloom <= days:
                flowers += 1
                if flowers == k:
                    bouquets += 1
                    flowers = 0
            else:
                flowers = 0
        return bouquets >= m