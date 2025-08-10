class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        tree, words, n = collections.defaultdict(set), set(wordList), len(beginWord)
        if endWord not in words:
            return []
        layer = {beginWord}
        while layer:
            newlayer = collections.defaultdict(set)
            for w in layer:
                if w == endWord:
                    return self.paths(tree, beginWord, endWord)
                for i in range(n):
                    for c in string.ascii_lowercase:
                        neww = w[:i]+c+w[i+1:]
                        if neww in words and neww != w and neww not in tree:
                            newlayer[neww].add(w)
            layer = newlayer
            for k, v in newlayer.items():
                tree[k] = v
        return []
    
    def paths(self, tree, beginWord, endWord):
        ans = [[endWord]]
        while ans[0][0] != beginWord:
            ans = [[p for k in ans for p in tree[k]] + an for an in ans]
        return ans
