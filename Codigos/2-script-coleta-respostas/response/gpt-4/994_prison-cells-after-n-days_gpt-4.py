class Solution:
    def prisonAfterNDays(self, cells, n):
        seen = {}
        while n > 0:
            state = tuple(cells)
            if state in seen:
                n %= seen[state] - n  
            seen[state] = n  
            if n == 0:
                break  
            next_day_cells = [0] * len(cells)
            for i in range(1, 7):
                next_day_cells[i] = 1 if cells[i-1] == cells[i+1] else 0  
            cells = next_day_cells  
            n -= 1  
        return cells  