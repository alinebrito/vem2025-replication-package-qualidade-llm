class Solution:
    def findSubstring(self, s: str, words: list) -> list:
        if not s or not words:
            return []

        word_len = len(words[0])
        total_len = word_len * len(words)
        word_count = {}
        for word in words:
            if word not in word_count:
                word_count[word] =1
            else:
                word_count[word] += 1

        result = []
        for i in range(len(s) - total_len + 1):
            temp_count = {}
            for j in range(len(words)):
                word = s[i + j * word_len:i + (j + 1) * word_len]
                if word not in word_count:
                    break
                if word not in temp_count:
                    temp_count[word] = 1
                else:
                    temp_count[word] += 1
                if temp_count[word] > word_count[word]:
                    break
            else:
                result.append(i)

        return result