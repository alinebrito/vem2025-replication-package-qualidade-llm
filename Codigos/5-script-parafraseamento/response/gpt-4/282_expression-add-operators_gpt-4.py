class Solution:
    def addOperators(self, num, target):
        res, self.target = [], target
        
        def backtrack(index, prev_operand, current_operand, value):
            if index == len(num):
                if value == self.target and current_operand == 0:
                    res.append("".join(current_expr))
                return
            
            current_digit = num[index]
            index += 1
            
            backtrack(index, current_operand * 10 + int(current_digit), 0, value)

            if current_expr:
                current_expr.append('+')
                current_expr.append(current_digit)
                backtrack(index, int(current_digit), 0, value + current_operand)
                current_expr.pop()
                current_expr.pop()

                current_expr.append('-')
                current_expr.append(current_digit)
                backtrack(index, -int(current_digit), 0, value + current_operand)
                current_expr.pop()
                current_expr.pop()

                current_expr.append('*')
                current_expr.append(current_digit)
                backtrack(index, prev_operand * current_operand, 0, value - prev_operand + (prev_operand * current_operand))
                current_expr.pop()
                current_expr.pop()

        current_expr = []
        backtrack(0, 0, 0, 0)
        return res  