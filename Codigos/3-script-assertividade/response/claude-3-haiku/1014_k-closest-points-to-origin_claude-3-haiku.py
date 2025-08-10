class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return nsmallest(k, points, lambda x, y: x * x + y * y)