class Solution:
    def getSkyline(self, buildings):
        events = [(L, -H, R) for L, R, H in buildings] + [(R, 0, 0) for _, R, _ in buildings]
        events.sort()
        heights = [0]
        res = []
        for x, negH, R in events:
            while heights and heights[-1] <= -negH:
                heights.pop()
            if not heights or heights[-1] != -negH:
                res.append([x, -negH if negH else 0])
            heights.append(-negH if negH else 0)
        return res