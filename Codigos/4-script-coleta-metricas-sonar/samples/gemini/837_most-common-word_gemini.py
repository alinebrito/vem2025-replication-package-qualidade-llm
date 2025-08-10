class Solution:
    def mostCommonWord(self, paragraph, banned):
        for c in "!?',;.":
            paragraph = paragraph.replace(c, " ")
        paragraph = paragraph.lower()
        words = paragraph.split()
        dic = {}
        for word in words:
            if word not in banned:
                if word in dic:
                    dic[word] += 1
                else:
                    dic[word] = 1
        max_count = 0
        res = ""
        for key, value in dic.items():
            if value > max_count:
                res = key
                max_count = value
        return res