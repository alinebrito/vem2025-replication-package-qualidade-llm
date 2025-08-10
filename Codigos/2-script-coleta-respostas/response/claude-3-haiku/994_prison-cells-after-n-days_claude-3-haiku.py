class Solution:
    def nextday(self, cells):
        next_day_cells = [0] * len(cells)
        for i in range(len(cells)):
            if i == 0 or i == len(cells) - 1:
                next_day_cells[i] = 1 - cells[i]
            else:
                if cells[i-1] == cells[i+1]:
                    next_day_cells[i] = 1
                else:
                    next_day_cells[i] = 0
        return next_day_cells