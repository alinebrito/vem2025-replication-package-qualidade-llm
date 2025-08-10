class Solution:
    def exist(self, board, word):
        if not board:
            return False
        rows, cols = len(board), len(board[0])
        for i in range(rows):
            for j in range(cols):
                if dfs(board, word, i, j):
                    return True
        return False

def dfs(board, word, i, j):
    if len(word) == 0:
        return True
    if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[0]:
        return False
    temp, board[i][j] = board[i][j], '/'  # avoid reusing the same cell
    found = dfs(board, word[1:], i + 1, j) or dfs(board, word[1:], i - 1, j) or dfs(board, word[1:], i, j + 1) or dfs(board, word[1:], i, j - 1)
    board[i][j] = temp
    return found