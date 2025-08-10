class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        (x0, y0), (x1, y1) = coordinates[: 2]
        for i in range(2, len(coordinates)):
            x, y = coordinates[i]
            if (x - x0) * (y1 - y0) != (x1 - x0) * (y - y0):
                return False
        return True