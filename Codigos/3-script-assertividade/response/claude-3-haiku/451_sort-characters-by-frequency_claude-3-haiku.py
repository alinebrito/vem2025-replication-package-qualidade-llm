class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}
        for c in s:
            freq[c] = freq.get(c, 0) + 1
        sorted_freq = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
        result = ''
        for c, count in sorted_freq:
            result += c * count
        return result