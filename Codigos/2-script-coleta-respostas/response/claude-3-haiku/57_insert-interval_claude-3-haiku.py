class Solution:
    def insert(self, intervals, newInterval):
        s, e = newInterval
        result = []
        i = 0
        while i < len(intervals) and intervals[i][1] < s:
            result.append(intervals[i])
            i += 1
        while i < len(intervals) and intervals[i][0] <= e:
            s = min(s, intervals[i][0])
            e = max(e, intervals[i][1])
            i += 1
        result.append([s, e])
        while i < len(intervals):
            result.append(intervals[i])
            i += 1
        return result