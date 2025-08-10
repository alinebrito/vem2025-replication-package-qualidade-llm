class Solution(object):
    def minDays(self, bloomDay, m, k):
        if m * k > len(bloomDay):
            return -1
        left, right = 1, max(bloomDay)
        while left < right:
            mid = (left + right) // 2
            count = bouquets = 0
            for bloom in bloomDay:
                if bloom <= mid:
                    count += 1
                else:
                    count = 0
                if count == k:
                    bouquets += 1
                    count = 0
            if bouquets >= m:
                right = mid
            else:
                left = mid + 1
        return left