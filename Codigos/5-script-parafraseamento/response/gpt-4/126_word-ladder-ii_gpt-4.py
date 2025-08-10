class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        tree, words, n = collections.defaultdict(set), set(wordList), len(beginWord)
        if endWord not in words: return []
        words.add(beginWord)
        
        found, layer = False, {beginWord}
        while layer and not found:
            next_layer = collections.defaultdict(set)
            for word in layer:
                for i in range(n):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        new_word = word[:i] + c + word[i+1:]
                        if new_word in words:
                            next_layer[new_word].add(word)
                            if new_word == endWord: found = True  
            words -= set(next_layer.keys())
            layer = next_layer
        
        res = []
        def backtrack(word):
            if word == beginWord: res.append([beginWord])
            for parent in tree[word]:
                for path in backtrack(parent):
                    res.append(path + [word])
            return res
        
        for word in next_layer:
            tree[word] = next_layer[word]
        
        return backtrack(endWord) if found else []