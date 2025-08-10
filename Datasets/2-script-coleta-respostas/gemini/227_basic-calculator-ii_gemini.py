class Solution:
    def calculate(self, s):
        if not s:
            return 0
        s = s.replace(" ", "")
        n = len(s)
        stack = []
        num = 0
        op = '+'
        for i in range(n):
            c = s[i]
            if c.isdigit():
                num = num * 10 + int(c)
            if not c.isdigit() or i == n - 1:
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == '*':
                    stack.append(stack.pop() * num)
                elif op == '/':
                    stack.append(int(stack.pop() / num))
                num = 0
                op = c
        return sum(stack)