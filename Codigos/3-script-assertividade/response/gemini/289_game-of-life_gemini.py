class Solution:
    def gameOfLifeInfinite(self, live):
        ctr = collections.Counter((I, J)
                                   for i, row in enumerate(live)
                                   for j, v in enumerate(row)
                                   if v
                                   for I in range(i - 1, i + 2)
                                   for J in range(j - 1, j + 2)
                                   if (I, J) != (i, j))
        return {(i, j)
                for (i, j), nei in ctr.items()
                if nei == 3 or nei == 2 and (i, j) in live}