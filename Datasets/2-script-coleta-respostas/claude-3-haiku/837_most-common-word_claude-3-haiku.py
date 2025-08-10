class Solution:
    def mostCommonWord(self, paragraph, banned):
        words = [word.strip("!?',;.") for word in paragraph.lower().split()]
        word_count = {}
        for word in words:
            if word not in banned:
                word_count[word] = word_count.get(word, 0) + 1
        return max(word_count, key=word_count.get)