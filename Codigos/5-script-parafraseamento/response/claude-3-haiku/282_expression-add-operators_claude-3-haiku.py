class Solution:
    def addOperators(self, num, target):
        res, self.target = [], target
        self.backtrack(num, target, 0, 0, 0, res)
        return res

    def backtrack(self, num, target, pos, eval, prev, res):
        if pos == len(num):
            if eval == target:
                res.append("".join(num))
            return
        for i in range(pos, len(num)):
            if i != pos and num[pos] == '0':
                break
            if pos == 0:
                self.backtrack(num, target, i+1, int(num[pos:i+1]), int(num[pos:i+1]), res)
            else:
                self.backtrack(num, target, i+1, eval + int(num[pos:i+1]), int(num[pos:i+1]), res)
                self.backtrack(num, target, i+1, eval - prev, -prev, res)