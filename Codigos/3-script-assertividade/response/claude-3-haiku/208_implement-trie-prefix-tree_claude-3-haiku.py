class Solution:
class Trie:
    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        node = self.trie
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node['end'] = True

    def search(self, word: str) -> bool:
        node = self.trie
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return 'end' in node

    def startsWith(self, prefix: str) -> bool:
        node = self.trie
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return True