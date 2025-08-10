class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}
        for w in words:
            node = trie
            for ch in w:
                node = node.setdefault(ch, {})
            node['#'] = w

        def dfs(i, j, node, path):
            if '#' in node:
                res.append(node['#'])
                del node['#']
            temp, board[i][j] = board[i][j], '/'
            for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] in node:
                    dfs(x, y, node[board[x][y]], path + board[x][y])
            board[i][j] = temp

        res = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in trie:
                    dfs(i, j, trie[board[i][j]], board[i][j])
        return res