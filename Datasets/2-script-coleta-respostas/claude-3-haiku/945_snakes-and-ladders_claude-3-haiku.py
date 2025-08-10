class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        
        def get_next_square(pos):
            row, col = divmod(pos - 1, n)
            row = n - 1 - row
            if row % 2 == 0:
                col = n - 1 - col
            return board[row][col] if board[row][col] != -1 else pos
        
        queue = deque([(1, 0)])
        visited = set()
        
        while queue:
            curr, moves = queue.popleft()
            if curr == n ** 2:
                return moves
            
            for next_square in range(curr + 1, min(curr + 7, n ** 2 + 1)):
                dest = get_next_square(next_square)
                if dest not in visited:
                    visited.add(dest)
                    queue.append((dest, moves + 1))
        
        return -1