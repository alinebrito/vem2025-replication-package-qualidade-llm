class Solution:
    def minDeletions(self, s: str) -> int:
 freq = {}
        for char in s:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
        
        freq_values = sorted(list(freq.values()), reverse=True)
        deletions = 0
        for i in range(1, len(freq_values)):
            while freq_values[i] >= freq_values[i-1]:
                freq_values[i] -= 1
                deletions += 1
        return deletions