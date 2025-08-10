class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1
        length = 0
        for c in count.values():
            length += c // 2 * 2
            if length % 2 == 0 and c % 2 == 1:
                length += 1
        return length