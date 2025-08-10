class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count
        result = []
        if len(s) < total_len:
            return result
        word_freq = {}
        for word in words:
            word_freq[word] = word_freq.get(word, 0) + 1
        for i in range(len(s) - total_len + 1):
            seen = {}
            j = 0
            while j < word_count:
                word = s[i+j*word_len:i+(j+1)*word_len]
                if word not in word_freq:
                    break
                seen[word] = seen.get(word, 0) + 1
                if seen[word] > word_freq[word]:
                    break
                j += 1
            else:
                result.append(i)
        return result