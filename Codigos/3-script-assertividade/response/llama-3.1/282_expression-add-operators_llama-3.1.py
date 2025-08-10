class Solution:
    def addOperators(self, num, target):
        res, self.target = [], target
        self.dfs(num, 0, "", 0, 0)
        return res

    def dfs(self, num, pos, path, cur_val, last_val):
        if pos == len(num):
            if cur_val == self.target:
                res.append(path)
            return

        for i in range(pos, len(num)):
            if i!= pos and num[pos] == "0":
                break
            str_val = num[pos:i+1]
            val = int(str_val)
            if pos == 0:
                self.dfs(num, i+1, path + str_val, val, val)
            else:
                self.dfs(num, i+1, path + "+" + str_val, cur_val + val, val)
                self.dfs(num, i+1, path + "-" + str_val, cur_val - val, -val)
                self.dfs(num, i+1, path + "*" + str_val, cur_val - last_val + last_val * val, last_val * val)