class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1
        sorted_chars = sorted(freq.items(), key=lambda x: -x[1])
        return ''.join(char * count for char, count in sorted_chars)