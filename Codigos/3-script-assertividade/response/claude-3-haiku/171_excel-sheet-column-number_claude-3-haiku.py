class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans, pos = 0, 0
        for char in columnTitle[::-1]:
            ans += (ord(char) - ord('A') + 1) * (26 ** pos)
            pos += 1
        return ans