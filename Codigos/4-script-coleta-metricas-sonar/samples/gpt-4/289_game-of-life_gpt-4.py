class Solution:
    def gameOfLifeInfinite(self, live):
        ctr = collections.Counter((i, j) for i, j in live)
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        next_gen = set()
        for (i, j), count in ctr.items():
            if count < 2 or count > 3:
                continue
            next_gen.add((i, j))
            for di, dj in directions:
                next_gen.add((i + di, j + dj))
        result = set()
        for cell in next_gen:
            count = sum((cell[0] + di, cell[1] + dj) in ctr for di, dj in directions)
            if count == 3 or (count == 2 and cell in ctr):
                result.add(cell)
        return result