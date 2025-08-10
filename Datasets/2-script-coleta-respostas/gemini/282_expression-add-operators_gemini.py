class Solution:
    def addOperators(self, num, target):
        res, self.target = [], target
        self.backtrack(num, 0, 0, 0, "", res)
        return res
        
    def backtrack(self, num, index, prev, curr, expression, res):
        if index == len(num):
            if curr == self.target:
                res.append(expression)
            return
        
        for i in range(index + 1, len(num) + 1):
            if i > index + 1 and num[index] == '0':
                break
            val = int(num[index:i])
            if index == 0:
                self.backtrack(num, i, val, val, str(val), res)
            else:
                self.backtrack(num, i,  val, curr + val, expression + "+" + str(val), res)
                self.backtrack(num, i, -val, curr - val, expression + "-" + str(val), res)
                self.backtrack(num, i, prev * val, curr - prev + prev * val, expression + "*" + str(val), res)