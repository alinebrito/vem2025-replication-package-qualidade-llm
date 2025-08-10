class Solution:
    def combinationSum(self, candidates, target):
        ret = []
        self.backtrack(candidates, target, 0, [], ret)
        return ret

    def backtrack(self, candidates, target, start, path, ret):
        if target < 0:
            return
        elif target == 0:
            ret.append(path[:])
        else:
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                self.backtrack(candidates, target - candidates[i], i, path, ret)
                path.pop()