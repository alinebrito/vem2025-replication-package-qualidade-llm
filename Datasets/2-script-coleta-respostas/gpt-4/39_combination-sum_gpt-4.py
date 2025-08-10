class Solution:
    def combinationSum(self, candidates, target):
        ret = []
        
        def backtrack(remain, path, start):
            if remain < 0:
                return
            if remain == 0:
                ret.append(path)
                return
            for i in range(start, len(candidates)):
                backtrack(remain - candidates[i], path + [candidates[i]], i)

        backtrack(target, [], 0)
        return ret