class Solution:
    def calculate(self, s):
        s = s.replace(" ", "")
        stack = []
        num = 0
        sign = 1
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            if (not s[i].isdigit() and not s[i].isspace()) or i == len(s) - 1:
                if s[i] == '+':
                    stack.append(num * sign)
                elif s[i] == '-':
                    stack.append(-num * sign)
                elif s[i] == '*':
                    stack.append(stack.pop() * num)
                elif s[i] == '/':
                    stack.append(int(stack.pop() / num))
                num = 0
                sign = 1 if s[i] in ['+', '*'] else -1 if s[i] == '-' else 0
        return sum(stack)