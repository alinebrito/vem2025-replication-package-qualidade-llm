class Solution:
    def exist(self, board, word):
 def dfs(i, j, k):
 if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or board[i][j] != word[k]:
 return False
            if k == len(word) - 1:
                return True
            temp, board[i][j] = board[i][j], '/'
            for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if dfs(i + x, j + y, k + 1):
                    return True
            board[i][j] = temp
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
 return True
        return False