class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, path, target):
            if target == 0:
                res.append(path)
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > target:
                    break
                backtrack(i + 1, path + [candidates[i]], target - candidates[i])
        
        candidates.sort()
        res = []
        backtrack(0, [], target)
        return res