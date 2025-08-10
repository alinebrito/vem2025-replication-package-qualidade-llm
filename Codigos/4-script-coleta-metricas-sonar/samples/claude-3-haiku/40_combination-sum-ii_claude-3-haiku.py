class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        
        result = []
        self.backtrack(candidates, target, 0, [], result)
        return result
    
    def backtrack(self, candidates, target, start, path, result):
        if target < 0:
            return
        elif target == 0:
            result.append(path[:])
        else:
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                self.backtrack(candidates, target - candidates[i], i + 1, path, result)
                path.pop()