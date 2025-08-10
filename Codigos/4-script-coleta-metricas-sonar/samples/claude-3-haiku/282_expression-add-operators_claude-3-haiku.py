class Solution:
    def addOperators(self, num, target):
        res, self.target = [], target
        self.dfs(num, 0, 0, 0, res)
        return res

    def dfs(self, num, pos, eval_so_far, prev, res):
        if pos == len(num):
            if eval_so_far == self.target:
                res.append(''.join(num))
            return

        for i in range(pos, len(num)):
            if i != pos and num[pos] == '0':
                break
            curr = int(num[pos:i+1])
            if pos == 0:
                self.dfs(num, i+1, curr, curr, res)
            else:
                self.dfs(num, i+1, eval_so_far + curr, curr, res)
                self.dfs(num, i+1, eval_so_far - prev, -prev, res)
                self.dfs(num, i+1, eval_so_far - prev + prev*curr, prev*curr, res)