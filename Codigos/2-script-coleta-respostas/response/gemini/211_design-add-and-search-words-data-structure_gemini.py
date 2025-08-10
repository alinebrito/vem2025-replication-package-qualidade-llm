class Solution:
    def __init__(self):
        self.trie = {}

    def addWord(self, word):
        node = self.trie
        for char in word:
            if char not in node:
                node[char] = {}