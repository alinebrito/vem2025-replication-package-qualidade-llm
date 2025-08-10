class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        result = list(words[0])
        for word in words[1:]:
            result = [c for c in result if c in word]
            for c in set(word):
                result[result.index(c)] = min(result.count(c), word.count(c)) * c
        return result