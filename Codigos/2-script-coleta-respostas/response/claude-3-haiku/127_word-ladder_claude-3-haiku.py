class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        wordList = set(wordList)
        queue = [beginWord]
        level = 1
        while queue:
            for _ in range(len(queue)):
                word = queue.pop(0)
                if word == endWord:
                    return level
                for i in range(len(word)):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        next_word = word[:i] + c + word[i+1:]
                        if next_word in wordList:
                            queue.append(next_word)
                            wordList.remove(next_word)
            level += 1
        return 0