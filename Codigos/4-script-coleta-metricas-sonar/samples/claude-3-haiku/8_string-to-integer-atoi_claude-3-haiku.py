class Solution:
    def myAtoi(self, s: str) -> int:
        value, state, pos, sign = 0, 0, 0, 1
        for char in s:
            if state == 0 and char == ' ':
                continue
            elif state == 0 and char in ['-', '+']:
                sign = -1 if char == '-' else 1
                state = 1
            elif char.isdigit():
                value = value * 10 + int(char)
                state = 1
            else:
                break
        value *= sign
        return max(-2**31, min(value, 2**31 - 1))