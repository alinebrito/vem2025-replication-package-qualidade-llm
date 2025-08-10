class Solution:
    def calculate(self, s):
        stack = []
        current_number = 0
        result = 0
        sign = 1
        
        for char in s:
            if char.isdigit():
                current_number = current_number * 10 + int(char)
            elif char in "+-":
                result += sign * current_number
                current_number = 0
                sign = 1 if char == '+' else -1
            elif char == '(':
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif char == ')':
                result += sign * current_number
                result *= stack.pop()
                result += stack.pop()
                current_number = 0
        
        result += sign * current_number
        return result