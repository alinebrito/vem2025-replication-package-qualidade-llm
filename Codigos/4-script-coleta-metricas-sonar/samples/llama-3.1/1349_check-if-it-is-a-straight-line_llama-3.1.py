class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        (x0, y0), (x1, y1) = coordinates[:2]
        return x1 - x0 == 0 or y1 - y0 == 0