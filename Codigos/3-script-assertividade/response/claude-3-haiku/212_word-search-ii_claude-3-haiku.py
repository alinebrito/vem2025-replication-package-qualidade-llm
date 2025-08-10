class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        res = []
        for word in words:
            for i in range(m):
                for j in range(n):
                    if self.dfs(board, i, j, word, 0):
                        res.append(word)
                        break
        return res

    def dfs(self, board, i, j, word, idx):
        if idx == len(word):
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[idx]:
            return False
        board[i][j] = '#'
        res = self.dfs(board, i+1, j, word, idx+1) or \
              self.dfs(board, i-1, j, word, idx+1) or \
              self.dfs(board, i, j+1, word, idx+1) or \
              self.dfs(board, i, j-1, word, idx+1)
        board[i][j] = word[idx]
        return res