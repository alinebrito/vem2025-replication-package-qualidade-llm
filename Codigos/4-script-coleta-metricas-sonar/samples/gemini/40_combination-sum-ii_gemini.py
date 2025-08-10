class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates: return []
        result = []
        candidates.sort()
        self.backtrack(candidates, target, 0, [], result)
        return result
    
    def backtrack(self, candidates, target, start, combination, result):
        if target == 0:
            result.append(combination.copy())
            return
        
        if target < 0:
            return
        
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            combination.append(candidates[i])
            self.backtrack(candidates, target - candidates[i], i + 1, combination, result)
            combination.pop()