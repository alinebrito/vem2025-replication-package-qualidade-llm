class Solution:
    def myAtoi(self, s: str) -> int:
        value, state, pos, sign = 0, 0, 0, 1

        while pos < len(s):
            char = s[pos]

            if state == 0:
                if char == ' ':
                    pos += 1
                elif char == '-':
                    sign = -1
                    state = 1
                elif char == '+':
                    state = 1
                elif char.isdigit():
                    value = int(char)
                    state = 2
                else:
                    break
            elif state == 1 or state == 2:
                if char.isdigit():
                    value = value * 10 + int(char)
                    state = 2
                else:
                    break
            pos += 1

        value = value * sign
        if value < -2**31:
            return -2**31
        elif value > 2**31 - 1:
            return 2**31 - 1
        else:
            return value