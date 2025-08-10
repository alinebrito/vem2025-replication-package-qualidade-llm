class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        tree, words, n = {}, set(wordList), len(beginWord)
        if endWord not in words:
            return []
        queue = [[beginWord]]
        found = False
        while queue and not found:
            visited = set()
            for _ in range(len(queue)):
                path = queue.pop(0)
                word = path[-1]
                for i in range(n):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        new_word = word[:i] + c + word[i + 1:]
                        if new_word in words:
                            if new_word == endWord:
                                found = True
                            if new_word not in tree:
                                tree[new_word] = []
                            tree[new_word].append(path + [new_word])
                            visited.add(new_word)
            words -= visited
            queue.extend(tree.get(endWord, []))
        return tree.get(endWord, [])