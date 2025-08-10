class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) == 0 or k > len(s):
            return 0

        if k == 1:
            return len(s)

        for char in set(s):
            if s.count(char) < k:
                return max(self.longestSubstring(substring, k) for substring in s.split(char))

        return len(s)