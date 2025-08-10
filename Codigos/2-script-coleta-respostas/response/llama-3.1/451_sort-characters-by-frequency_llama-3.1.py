class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}
        for char in s:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
        sorted_chars = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        result = ''
        for char, count in sorted_chars:
            result += char * count
        return result