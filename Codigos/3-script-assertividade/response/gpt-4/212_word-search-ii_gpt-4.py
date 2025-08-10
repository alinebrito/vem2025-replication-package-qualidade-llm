class Solution:
    def findWords(self, board, words):
        class TrieNode:
            def __init__(self):
                self.children = {}
                self.is_end = False

        def build_trie(words):
            root = TrieNode()
            for word in words:
                node = root
                for char in word:
                    if char not in node.children:
                        node.children[char] = TrieNode()
                    node = node.children[char]
                node.is_end = True
            return root

        def backtrack(x, y, node, path):
            if node.is_end:
                result.add(path)
                node.is_end = False
            if not (0 <= x < len(board) and 0 <= y < len(board[0])) or (x, y) in visited or board[x][y] not in node.children:
                return
            visited.add((x, y))
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                backtrack(x + dx, y + dy, node.children[board[x][y]], path + board[x][y])
            visited.remove((x, y))

        root = build_trie(words)
        result = set()
        visited = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                backtrack(i, j, root, "")
        return list(result)