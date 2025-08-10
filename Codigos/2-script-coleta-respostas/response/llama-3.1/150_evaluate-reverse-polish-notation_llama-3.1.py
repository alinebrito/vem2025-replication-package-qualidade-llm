class Solution:
    def evalRPN(self, tokens):
        stack = []
        for token in tokens:
            if token in {"+", "-", "*", "/"}:
                r, l = stack.pop(), stack.pop()
                if token == "+":
                    stack.append(l + r)
                elif token == "-":
                    stack.append(l - r)
                elif token == "*":
                    stack.append(l * r)
                else:
                    stack.append(int(l / r))
            else:
                stack.append(int(token))
        return stack[0]