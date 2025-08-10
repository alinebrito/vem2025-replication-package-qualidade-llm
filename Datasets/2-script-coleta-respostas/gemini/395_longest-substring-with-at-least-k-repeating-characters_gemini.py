class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) == 0 or k > len(s):
            return 0
        if k == 1:
            return len(s)
        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
        idx = 0
        while idx < len(s) and count[ord(s[idx]) - ord('a')] >= k:
            idx += 1
        if idx == len(s):
            return len(s)
        left = self.longestSubstring(s[:idx], k)
        right = self.longestSubstring(s[idx + 1:], k)
        return max(left, right)