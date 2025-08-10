class Solution:
    def getSkyline(self, buildings):
        events = [(L, -H, R) for L, R, H in buildings] + [(R, 0, 0) for _, R, _ in buildings]
        events.sort()
        active = [0]
        result = []
        for pos, negH, R in events:
            while active and active[-1][1] == negH:
                active.pop()
            active.append((pos, negH))
            active.sort()
            if not result or active[-1][0] != result[-1][0]:
                result.append((active[-1][0], active[-1][1]))
        return result