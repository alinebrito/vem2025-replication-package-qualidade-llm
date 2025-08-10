class Solution:
    def kClosest(self, points, k):
        return sorted(points, key=lambda x: x[0]**2 + x[1]**2)[:k]