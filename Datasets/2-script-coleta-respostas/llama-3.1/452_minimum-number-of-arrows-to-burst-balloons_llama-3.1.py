class Solution:
    def findMinArrowShots(self, points):
        if not points:
            return 0
        points.sort(key=lambda p: p[1])
        arrows = 1
        end = points[0][1]
        for start, end2 in points[1:]:
            if start > end:
                arrows += 1
                end = end2
            else:
                end = min(end, end2)
        return arrows