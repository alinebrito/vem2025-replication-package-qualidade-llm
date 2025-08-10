class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque  
        rotten = deque()
        fresh_count = 0  
        minutes = 0  
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    rotten.append((i, j))
                elif grid[i][j] == 1:
                    fresh_count += 1
        
        while rotten and fresh_count > 0:
            for _ in range(len(rotten)):
                x, y = rotten.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy  
                    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 1:
                        grid[nx][ny] = 2  
                        fresh_count -= 1  
                        rotten.append((nx, ny))
            minutes += 1
        
        return minutes if fresh_count == 0 else -1  