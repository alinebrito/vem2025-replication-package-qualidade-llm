class Solution:
    def combinationSum(self, candidates, target):
        ret = []
        self.dfs(candidates, target, [], 0, ret)
        return ret

    def dfs(self, candidates, target, path, start, ret):
        if target < 0:
            return
        if target == 0:
            ret.append(path)
            return
        for i in range(start, len(candidates)):
            self.dfs(candidates, target - candidates[i], path + [candidates[i]], i, ret)