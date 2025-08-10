class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        tree, words, n = dict(), set(wordList), len(beginWord)
        if endWord not in words:
            return []
        tree[beginWord] = set()
        tree[endWord] = set()
        words.add(beginWord)
        found, q, nq = False, [beginWord], []
        while q and not found:
            for x in q:
                for y in range(n):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        temp = x[:y] + c + x[y + 1:]
                        if temp not in words:
                            continue
                        if temp not in tree:
                            tree[temp] = set()
                        tree[temp].add(x)
                        if temp == endWord:
                            found = True
                        else:
                            nq.append(temp)
            q, nq = nq, []
        return self.backtrack(tree, beginWord, endWord) if found else []

    def backtrack(self, tree, beginWord, endWord):
        ans = [[endWord]]
        while ans[0][0]!= beginWord:
            temp = []
            for x in ans:
                for y in tree[x[0]]:
                    temp.append([y] + x)
            ans = temp