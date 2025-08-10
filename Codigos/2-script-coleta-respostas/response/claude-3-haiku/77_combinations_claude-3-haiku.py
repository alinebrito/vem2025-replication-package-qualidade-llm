class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(candidate):
            if len(candidate) == k:
                output.append(candidate[:])
                return
            
            start = candidate[-1] + 1 if candidate else 1
            for num in range(start, n + 1):
                candidate.append(num)
                backtrack(candidate)
                candidate.pop()
        
        output = []
        backtrack([])
        return output