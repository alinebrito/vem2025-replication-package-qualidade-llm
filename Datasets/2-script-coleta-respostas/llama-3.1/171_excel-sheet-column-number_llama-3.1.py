class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans, pos = 0, 0
        for c in columnTitle:
            ans += (ord(c) - ord('A') + 1) * (26 ** pos)
            pos += 1
        return ans