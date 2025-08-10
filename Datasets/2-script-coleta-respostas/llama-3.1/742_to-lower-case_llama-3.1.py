class Solution:
    def toLowerCase(self, s: str) -> str:
        ans = ""
        for char in s:
            if char.isupper():
                ans += char.lower()
            else:
                ans += char
        return ans