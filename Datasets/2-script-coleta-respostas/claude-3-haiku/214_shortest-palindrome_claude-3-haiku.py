class Solution:
    def shortestPalindrome(self, s: str) -> str:
        r = s[::-1]
        for i in range(len(s)):
            if s[:len(s)-i] == r[i:]:
                return r[:i] + s
        return r + s