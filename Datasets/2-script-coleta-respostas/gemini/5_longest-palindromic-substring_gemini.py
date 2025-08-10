class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        start = 0
        max_length = 1

        for i in range(1, len(s)):
            # Odd-length palindromes
            left = i - 1
            right = i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > max_length:
                    start = left
                    max_length = right - left + 1
                left -= 1
                right += 1

            # Even-length palindromes
            left = i - 1
            right = i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > max_length:
                    start = left
                    max_length = right - left + 1
                left -= 1
                right += 1

        return s[start:start + max_length]