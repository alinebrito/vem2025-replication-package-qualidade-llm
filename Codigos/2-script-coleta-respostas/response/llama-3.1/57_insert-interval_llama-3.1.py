class Solution:
    def insert(self, intervals, newInterval):
        start, end = newInterval
        left, right = [], []
        for i in intervals:
            if i[1] < start:
                left += [i]
            elif i[0] > end:
                right += [i]
            else:
                start = min(start, i[0])
                end = max(end, i[1])
        return left + [[start, end]] + right