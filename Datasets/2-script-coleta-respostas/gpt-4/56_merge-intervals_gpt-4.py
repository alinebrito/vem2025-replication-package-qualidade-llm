class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])
        out = []
        for interval in intervals:
            if not out or out[-1][1] < interval[0]:
                out.append(interval)
            else:
                out[-1][1] = max(out[-1][1], interval[1])
        return out