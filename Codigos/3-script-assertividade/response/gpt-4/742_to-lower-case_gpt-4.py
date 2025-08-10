class Solution:
    def toLowerCase(self, s: str) -> str:
        ans = ""
        for char in s:
            if 'A' <= char <= 'Z':
                ans += chr(ord(char) + 32)
            else:
                ans += char
        return ans