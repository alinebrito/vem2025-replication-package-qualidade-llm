class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s:
            return 0
        sign = 1
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]
        num = 0
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            else:
                break
        num *= sign
        num = max(-2**31, min(num, 2**31 - 1))
        return num