class Solution:
    def findWords(self, board, words):
        self.rows = len(board)
        self.cols = len(board[0])
        self.trie = Trie()
        for word in words:
            self.trie.insert(word)

        res = set()
        for row in range(self.rows):
            for col in range(self.cols):
                self.dfs(board, row, col, "", self.trie, res)
        return list(res)

    def dfs(self, board, row, col, path, trie, res):
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols or board[row][col] == "#":
            return
        currChar = board[row][col]
        board[row][col] = "#"
        path += currChar

        if trie.children.get(currChar):
            if trie.children[currChar].isEnd:
                res.add(path)

            self.dfs(board, row + 1, col, path, trie.children[currChar], res)
            self.dfs(board, row - 1, col, path, trie.children[currChar], res)
            self.dfs(board, row, col + 1, path, trie.children[currChar], res)
            self.dfs(board, row, col - 1, path, trie.children[currChar], res)
        board[row][col] = currChar


class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.isEnd = True