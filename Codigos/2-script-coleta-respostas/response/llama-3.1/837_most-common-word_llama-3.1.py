class Solution:
    def mostCommonWord(self, paragraph, banned):
        words = ''.join(e for e in paragraph if e.isalnum() or e.isspace()).lower().split()
        word_count = {}
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1
        for word in banned:
            if word in word_count:
                del word_count[word]
        return max(word_count, key=word_count.get)