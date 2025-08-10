class Solution:
    def gameOfLifeInfinite(self, live):
        ctr = collections.Counter((i + di, j + dj) for i, j in live for di in (-1, 0, 1) for dj in (-1, 0, 1))
        return {cell for cell, count in ctr.items() if count == 3 or (count == 2 and cell in live)}