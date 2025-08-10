class Solution:
    def calculate(self, s):
        total = 0
        stack = []
        num = 0
        sign = 1

        for i, char in enumerate(s):
            if char.isdigit():
                num = num * 10 + int(char)
            if char in ['+', '-']:
                total += sign * num
                num = 0
                sign = 1 if char == '+' else -1
            if char == '(':
                stack.append(total)
                stack.append(sign)
                total = 0
                sign = 1
            if char == ')':
                total += sign * num
                num = 0
                total *= stack.pop()
                total += stack.pop()
        total += sign * num
        return total