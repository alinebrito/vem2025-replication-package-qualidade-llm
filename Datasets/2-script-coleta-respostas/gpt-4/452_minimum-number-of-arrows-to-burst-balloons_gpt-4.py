class Solution:
    def findMinArrowShots(self, segments):
        segments.sort(key=lambda p: p[1])
        arrows = 0
        end = float('-inf')
        for start, e in segments:
            if start > end:
                arrows += 1
                end = e
        return arrows