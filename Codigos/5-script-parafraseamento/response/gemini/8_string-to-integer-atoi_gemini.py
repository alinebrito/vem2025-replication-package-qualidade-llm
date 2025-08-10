class Solution:
    def myAtoi(self, str: str) -> int:
        value, state, pos, sign = 0, 0, 0, 1
        while pos < len(str) and str[pos] == ' ':
            pos += 1
        if pos < len(str) and (str[pos] == '-' or str[pos] == '+'):
            if str[pos] == '-':
                sign = -1
            pos += 1
        while pos < len(str) and '0' <= str[pos] <= '9':
            value = value * 10 + int(str[pos])
            if value > (2**31 - 1):
                return (2**31 - 1) if sign > 0 else -2**31
            pos += 1