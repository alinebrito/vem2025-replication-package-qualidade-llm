class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        seen = {}
        for i in range(n):
            next_day_cells = [0] * len(cells)
            for j in range(1, 7):
 if cells[j-1] == cells[j+1]:
                    next_day_cells[j] = 1
                else:
                    next_day_cells[j] = 0 if tuple(next_day_cells) in seen:
                i = (n - 1) % (i - seen[tuple(next_day_cells)]) + i
                break
            seen[tuple(next_day_cells)] = i
            cells = next_day_cells
        return cells