class Solution:
    def gameOfLifeInfinite(self, live):
        ctr = collections.Counter((i, j) for i, j in live for di in (-1, 0, 1) for dj in (-1, 0, 1) if (di, dj) != (0, 0))
        return {(i, j) for (i, j), c in ctr.items() if c == 3 or c == 2 and (i, j) in live}