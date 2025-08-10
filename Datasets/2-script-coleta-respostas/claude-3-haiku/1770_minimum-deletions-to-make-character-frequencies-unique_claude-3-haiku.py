class Solution:
    def minDeletions(self, s: str) -> int:
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1
        seen = set()
        deletions = 0
        for f in freq.values():
            while f in seen and f > 0:
                f -= 1
                deletions += 1
            seen.add(f)
        return deletions