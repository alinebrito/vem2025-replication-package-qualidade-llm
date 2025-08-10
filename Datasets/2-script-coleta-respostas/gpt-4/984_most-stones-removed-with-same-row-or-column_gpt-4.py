class Solution:
    def removeStones(self, stones):
        rows = {}
        cols = {}
        for x, y in stones:
            if x not in rows:
                rows[x] = []
            if y not in cols:
                cols[y] = []
            rows[x].append((x, y))
            cols[y].append((x, y))
        
        visited = set()
        def dfs(stone):
            x, y = stone
            for nx, ny in rows[x]:
                if (nx, ny) not in visited:
                    visited.add((nx, ny))
                    dfs((nx, ny))
            for nx, ny in cols[y]:
                if (nx, ny) not in visited:
                    visited.add((nx, ny))
                    dfs((nx, ny))
        
        components = 0
        for stone in stones:
            if stone not in visited:
                dfs(stone)
                components += 1
        
        return len(stones) - components