class Solution:
    def myAtoi(self, s: str) -> int:
        value, sign, i = 0, 1, 0
        INT_MAX, INT_MIN = 2**31 - 1, -2**31
        
        while i < len(s) and s[i] == ' ':
            i += 1
        
        if i < len(s) and (s[i] == '-' or s[i] == '+'):
            sign = -1 if s[i] == '-' else 1
            i += 1
        
        while i < len(s) and s[i] == '0':
            i += 1
        
        while i < len(s) and s[i].isdigit():
            digit = int(s[i])
            if value > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN
            value = value * 10 + digit
            i += 1
        
        return sign * value