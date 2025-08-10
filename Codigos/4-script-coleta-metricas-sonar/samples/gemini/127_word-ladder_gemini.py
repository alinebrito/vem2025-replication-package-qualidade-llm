class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        if endWord not in wordList:
            return 0
        wordSet = set(wordList)
        queue = [(beginWord, 1)]
        visited = set([beginWord])
        while queue:
            word, length = queue.pop(0)
            if word == endWord:
                return length
            for i in range(len(word)):
                for char in 'abcdefghijklmnopqrstuvwxyz':
                    newWord = word[:i] + char + word[i+1:]
                    if newWord in wordSet and newWord not in visited:
                        queue.append((newWord, length + 1))
                        visited.add(newWord)
        return 0