class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count
        word_map = {}
        for word in words:
            if word in word_map:
                word_map[word] += 1
            else:
                word_map[word] = 1
        result = []
        for i in range(len(s) - total_len + 1):
            seen = {}
            for j in range(word_count):
                word_index = i + j * word_len
                word = s[word_index:word_index + word_len]
                if word in word_map:
                    if word in seen:
                        seen[word] += 1
                    else:
                        seen[word] = 1
                    if seen[word] > word_map[word]:
                        break
                else:
                    break
            if seen == word_map:
                result.append(i)
        return result