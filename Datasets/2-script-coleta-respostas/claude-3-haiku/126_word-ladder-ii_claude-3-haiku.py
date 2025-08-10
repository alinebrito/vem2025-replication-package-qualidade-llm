class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        tree, words, n = collections.defaultdict(set), set(wordList), len(beginWord)
        if endWord not in words:
            return []
        forward, backward = {beginWord}, {endWord}
        while forward and backward:
            if len(forward) > len(backward):
                forward, backward = backward, forward
            new = set()
            for word in forward:
                for i in range(n):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        next_word = word[:i] + c + word[i+1:]
                        if next_word in backward:
                            return [[next_word] + path for path in self.findLadders(beginWord, next_word, wordList)]
                        if next_word in words:
                            new.add(next_word)
                            tree[next_word].add(word)
            forward = new
        return []