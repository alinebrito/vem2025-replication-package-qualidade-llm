class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        def get_position(x):
            row = (x - 1) // n
            col = (x - 1) % n if row % 2 == 0 else n - 1 - (x - 1) % n
            return n - 1 - row, col
        
        from collections import deque
        queue = deque([1])
        visited = set([1])
        moves = 0
        
        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr == n * n:
                    return moves
                for next in range(curr + 1, min(curr + 6, n * n) + 1):
                    r, c = get_position(next)
                    if board[r][c] != -1:
                        next = board[r][c]
                    if next not in visited:
                        visited.add(next)
                        queue.append(next)
            moves += 1
        return -1