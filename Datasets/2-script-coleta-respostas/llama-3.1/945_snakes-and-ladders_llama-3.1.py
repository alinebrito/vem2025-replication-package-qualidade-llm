class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        visited = [False] * (n * n + 1)
        queue = [(1, 0)]
        visited[1] = True
        while queue:
            curr, step = queue.pop(0)
            for next in range(curr + 1, min(curr + 7, n * n + 1)):
                r = (next - 1) // n
                c = (next - 1) % n
                if board[n - 1 - r][c if r % 2 == 0 else n - 1 - c] != -1:
                    next = board[n - 1 - r][c if r % 2 == 0 else n - 1 - c]
                if next == n * n:
                    return step + 1
                if not visited[next]:
                    visited[next] = True
                    queue.append((next, step + 1))
        return -1