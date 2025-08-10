class Solution(object):
    def countCharacters(self, words, chars):
        char_count = {}
        for char in chars:
            char_count[char] = char_count.get(char, 0) + 1
        total_length = 0
        for word in words:
            word_count = {}
            for char in word:
                word_count[char] = word_count.get(char, 0) + 1
            if all(word_count[char] <= char_count.get(char, 0) for char in word_count):
                total_length += len(word)
        return total_length