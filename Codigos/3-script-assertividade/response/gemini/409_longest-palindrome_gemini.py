class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = {}
        for c in s:
            count[c] = count.get(c, 0) + 1
        length = 0
        odd_found = False
        for c in count:
            if count[c] % 2 == 0:
                length += count[c]
            else:
                length += count[c] - 1
                odd_found = True
        if odd_found:
            length += 1
        return length