class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_len = len(words[0])
        total_len = word_len * len(words)
        result = []
        word_counts = {}
        for word in words:
            if word not in word_counts:
                word_counts[word] = 0
            word_counts[word] += 1

        for i in range(len(s) - total_len + 1):
            seen_words = {}
            j = 0
            while j < total_len:
                current_word = s[i + j:i + j + word_len]
                if current_word in word_counts:
                    if current_word not in seen_words:
                        seen_words[current_word] = 0
                    seen_words[current_word] += 1
                    if seen_words[current_word] > word_counts[current_word]:
                        break
                    j += word_len
                else:
                    break
            if j == total_len:
                result.append(i)
        return result