class Solution:
    def prisonAfterNDays(self, cells: list[int], n: int) -> list[int]:
        def nextday(cells):
            next_day_cells = [0] *len(cells)
            for i in range(1, len(cells) - 1):
                if cells[i - 1] == cells[i + 1]:
                    next_day_cells[i] = 1
                else:
                    next_day_cells[i] = 0
            return next_day_cells

        seen = {}
        while n > 0:
            c = tuple(cells)
            if c in seen:
                n %= seen[c] - n
            seen[c] = n
            if n >= 1:
                cells = nextday(cells)
                n -= 1
        return cells