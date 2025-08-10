class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        n = 9
        rows = [set() for _ in range(n)]
        cols = [set() for _ in range(n)]
        boxes = [set() for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if board[i][j] != ".":
                    val = board[i][j]
                    rows[i].add(val)
                    cols[j].add(val)
                    boxes[(i // 3) * 3 + j // 3].add(val)

        def backtrack(i, j):
            if i == n:
                return True
            if j == n:
                return backtrack(i + 1, 0)
            if board[i][j] != ".":
                return backtrack(i, j + 1)

            for val in range(1, 10):
                val = str(val)
                if (
                    val not in rows[i]
                    and val not in cols[j]
                    and val not in boxes[(i // 3) * 3 + j // 3]
                ):
                    board[i][j] = val
                    rows[i].add(val)
                    cols[j].add(val)
                    boxes[(i // 3) * 3 + j // 3].add(val)

                    if backtrack(i, j + 1):
                        return True

                    board[i][j] = "."
                    rows[i].remove(val)
                    cols[j].remove(val)
                    boxes[(i // 3) * 3 + j // 3].remove(val)
            return False

        backtrack(0, 0)