class Solution:
    def wordPattern(self, pattern, s):
        words = s.split()
        if len(pattern) != len(words):
            return False  
        char_to_word = {}
        word_to_char = {}
        for c, w in zip(pattern, words):
            if c not in char_to_word:
                char_to_word[c] = w  
            if w not in word_to_char:
                word_to_char[w] = c  
            if char_to_word[c] != w or word_to_char[w] != c:
                return False  
        return True  