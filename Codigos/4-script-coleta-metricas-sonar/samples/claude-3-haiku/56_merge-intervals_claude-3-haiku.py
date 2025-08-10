class Solution:
    def merge(self, intervals):
        out = []
        intervals.sort(key=lambda x: x[0])
        for i in intervals:
            if not out or out[-1][1] < i[0]:
                out.append(i)
            else:
                out[-1][1] = max(out[-1][1], i[1])
        return out