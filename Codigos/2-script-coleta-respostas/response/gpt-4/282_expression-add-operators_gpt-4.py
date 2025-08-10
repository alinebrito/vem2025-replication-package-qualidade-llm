class Solution:
    def addOperators(self, num, target):
        res, self.target = [], target
        
        def backtrack(index, prev_operand, current_operand, value, expression):
            if index == len(num):
                if value == self.target and current_operand == 0:
                    res.append(expression)
                return
            
            current_num = ""
            for i in range(index, len(num)):
                current_num += num[i]
                if len(current_num) > 1 and current_num[0] == '0':
                    break
                current_num_int = int(current_num)
                
                backtrack(i + 1, current_num_int, current_num_int, value + current_num_int, expression + "+" + current_num if expression else current_num)
                backtrack(i + 1, -current_num_int, current_num_int, value - current_num_int, expression + "-" + current_num)
                backtrack(i + 1, prev_operand * current_num_int, current_num_int, value - prev_operand + (prev_operand * current_num_int), expression + "*" + current_num)
        
        backtrack(0, 0, 0, 0, "")
        return res