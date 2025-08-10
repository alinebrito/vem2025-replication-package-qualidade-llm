class Solution:
class WordDictionary:
    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        node = self.trie
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node['#'] = True

    def search(self, word: str) -> bool:
        def dfs(node, i):
            curr = node
            for j in range(i, len(word)):
                char = word[j]
                if char == '.':
                    for child in curr.values():
                        if dfs(child, j+1):
                            return True
                    return False
                else:
                    if char not in curr:
                        return False
                    curr = curr[char]
            return '#' in curr
        return dfs(self.trie, 0)