class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        word_set = set(wordList)
        queue = [(beginWord, 1)]
        while queue:
            word, length = queue.pop(0)
            if word == endWord:
                return length
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    new_word = word[:i] + c + word[i+1:]
                    if new_word in word_set:
                        word_set.remove(new_word)
                        queue.append((new_word, length + 1))