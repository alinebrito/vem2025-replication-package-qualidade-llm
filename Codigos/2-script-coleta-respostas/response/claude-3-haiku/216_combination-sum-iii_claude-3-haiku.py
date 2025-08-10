class Solution:
    def combinationSum3(self, k, n):
        ret = []
        self.backtrack(k, n, 1, [], ret)
        return ret

    def backtrack(self, k, n, start, path, ret):
        if len(path) == k:
            if sum(path) == n:
                ret.append(path[:])
            return
        for i in range(start, 10):
            path.append(i)
            self.backtrack(k, n, i+1, path, ret)
            path.pop()