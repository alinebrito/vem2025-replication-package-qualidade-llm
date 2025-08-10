class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        count = 0
        last_end = -float('inf')
        for start, end in intervals:
            if start >= last_end:
                last_end = end
            else:
                count += 1
        return count