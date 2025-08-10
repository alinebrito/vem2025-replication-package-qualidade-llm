class Solution:
    def minDeletions(self, s: str) -> int:
        char_counts = [0] * 26
        for char in s:
            char_counts[ord(char) - ord('a')] += 1
        char_counts.sort(reverse=True)
        deletions = 0
        max_freq = char_counts[0]
        for i in range(1, 26):
            if char_counts[i] == 0:
                break
            if char_counts[i] >= max_freq:
                deletions += char_counts[i] - max_freq + 1
                max_freq -= 1
            else:
                max_freq = char_counts[i]
        return deletions