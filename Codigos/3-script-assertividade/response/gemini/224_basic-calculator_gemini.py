class Solution:
    def calculate(self, s):
        total = 0
        stack = []
        sign = 1
        num = 0
        i = 0

        while i < len(s):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            elif s[i] == "+":
                total += sign * num
                sign = 1
                num = 0
            elif s[i] == "-":
                total += sign * num
                sign = -1
                num = 0
            elif s[i] == "(":
                stack.append(total)
                stack.append(sign)
                total = 0
                sign = 1
            elif s[i] == ")":
                total += sign * num
                total *= stack.pop()
                total += stack.pop()
                num = 0
            i += 1
        return total + (sign * num)