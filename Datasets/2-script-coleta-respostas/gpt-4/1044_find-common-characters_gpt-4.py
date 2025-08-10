class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        result = []
        min_count = {char: float('inf') for char in set(''.join(words))}
        for word in words:
            count = {}
            for char in word:
                count[char] = count.get(char, 0) + 1  
            for char in min_count:
                min_count[char] = min(min_count[char], count.get(char, 0))
        for char, count in min_count.items():
            result.extend([char] * count)
        return result  