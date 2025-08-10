class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0

        queue = [(beginWord, 1)]
        while queue:
            word, length = queue.pop(0)
            if word == endWord:
                return length
            for i in range(len(word)):
                for char in 'abcdefghijklmnopqrstuvwxyz':
                    nextWord = word[:i] + char + word[i+1:]
                    if nextWord in wordSet:
                        wordSet.remove(nextWord)
                        queue.append((nextWord, length + 1))
        return 0