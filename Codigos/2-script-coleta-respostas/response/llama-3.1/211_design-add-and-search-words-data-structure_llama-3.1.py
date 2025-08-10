class Solution:
    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        node = self.trie
        for ch in word:
            node = node.setdefault(ch, {})
        node['$'] = True

    def search(self, word: str) -> bool:
        def dfs(node, idx):
            if idx == len(word):
                return '$' in node
            if word[idx] == '.':
                for ch in node:
                    if ch != '$' and dfs(node[ch], idx + 1):
                        return True
            elif word[idx] in node:
                if dfs(node[word[idx]], idx + 1):
                    return True
            return False

        return dfs(self.trie, 0)