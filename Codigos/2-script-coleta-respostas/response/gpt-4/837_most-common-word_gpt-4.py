class Solution:
    def mostCommonWord(self, paragraph, banned):
        paragraph = ''.join(c.lower() if c.isalnum() or c.isspace() else ' ' for c in paragraph)
        words = paragraph.split()
        count = {}
        for word in words:
            if word not in banned:
                count[word] = count.get(word, 0) + 1
        return max(count, key=count.get)