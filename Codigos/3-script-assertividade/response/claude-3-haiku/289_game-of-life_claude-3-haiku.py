class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        m, n = len(board), len(board[0])
        
        def get_neighbors(i, j):
            for di in [-1, 0, 1]:
                for dj in [-1, 0, 1]:
                    if di == dj == 0:
                        continue
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n:
                        yield ni, nj
        
        def count_live_neighbors(i, j):
            return sum(board[ni][nj] & 1 for ni, nj in get_neighbors(i, j))
        
        for i in range(m):
            for j in range(n):
                live_neighbors = count_live_neighbors(i, j)
                if board[i][j] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[i][j] = 1 | 2  # mark as dead
                else:
                    if live_neighbors == 3:
                        board[i][j] = 2  # mark as live
        
        for i in range(m):
            for j in range(n):
                board[i][j] >>= 1