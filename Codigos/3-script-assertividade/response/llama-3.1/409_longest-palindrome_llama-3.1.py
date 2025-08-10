class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_count = {}
        for char in s:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        
        length = 0
        odd_count = 0
        for count in char_count.values():
            length += count // 2 * 2            if count % 2 == 1:
                odd_count += 1
        
        if odd_count > 0:
            length += 1
        
        return length