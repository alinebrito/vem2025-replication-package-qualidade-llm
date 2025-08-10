class Solution:
    def minDeletions(self, s: str) -> int:
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1
        
        values = list(freq.values())
        unique_freq = set()
        deletions = 0
        
        for val in values:
            while val in unique_freq:
                val -= 1
                deletions += 1
            if val > 0:
                unique_freq.add(val)
        
        return deletions