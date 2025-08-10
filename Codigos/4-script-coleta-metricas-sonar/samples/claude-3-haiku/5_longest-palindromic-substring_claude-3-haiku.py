class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        
        max_len = 0
        start = 0
        
        for i in range(len(s)):
            # Odd-length palindromes
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > max_len:
                    max_len = right - left + 1
                    start = left
                left -= 1
                right += 1
            
            # Even-length palindromes
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > max_len:
                    max_len = right - left + 1
                    start = left
                left -= 1
                right += 1
        
        return s[start:start+max_len]