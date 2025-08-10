class Solution:
    def maxDistToClosest(self, seats):
        n = len(seats)
        left = [n] * n
        right = [n] * n
        l = r = n
        for i in range(n):
            if seats[i] == 1:
                l = i
            left[i] = l - i
            if i > 0:
                right[i - 1] = min(right[i - 1], i - r)
            if seats[n - i - 1] == 1:
                r = n - i - 1