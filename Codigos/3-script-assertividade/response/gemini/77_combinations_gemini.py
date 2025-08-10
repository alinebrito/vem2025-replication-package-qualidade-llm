class Solution:
    def combine(self, n, k):
        result = []
        def backtrack(combination, start):
            if len(combination) == k:
                result.append(combination.copy())
                return
            if start > n:
                return
            for i in range(start, n + 1):
                combination.append(i)
                backtrack(combination, i + 1)
                combination.pop()
        backtrack([], 1)
        return result