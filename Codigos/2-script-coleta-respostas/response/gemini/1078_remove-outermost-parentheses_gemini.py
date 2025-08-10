class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = ''
        opened = 0
        for c in s:
            if c == '(':
                opened += 1
                if opened > 1:
                    res += c
            else:
                opened -= 1
                if opened > 0:
                    res += c
        return res