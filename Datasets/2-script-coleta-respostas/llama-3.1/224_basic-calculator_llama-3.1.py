class Solution:
    def calculate(self, s: str) -> int:
        stack, curr_num, operation, sign = [], 0, [], '+'
        for c in s + '+':
            if c.isdigit():
                curr_num = curr_num * 10 + int(c)
            elif c in ['+', '-']:
                self.update(stack, curr_num, operation, sign)
                sign = c
                curr_num = 0
            elif c == '(':
                operation.append(sign)
                sign = '+'
                stack.append('(')
            elif c == ')':
                self.update(stack, curr_num, operation, sign)
                curr_num = 0
                while stack and stack[-1]!= '(':
                    stack.pop()
                stack.pop()
                if operation:
                    sign = operation.pop()
        return sum(stack)

    def update(self, stack, curr_num, operation, sign):
        if sign == '+':
            stack.append(curr_num)
        elif sign == '-':
            stack.append(-curr_num)