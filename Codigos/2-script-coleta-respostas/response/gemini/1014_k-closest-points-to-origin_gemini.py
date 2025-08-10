class Solution:
    def kClosest(self, points, k):
        return sorted(points, key=lambda point: point[0] ** 2 + point[1] ** 2)[:k]