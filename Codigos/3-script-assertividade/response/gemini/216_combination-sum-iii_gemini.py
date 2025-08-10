class Solution:
    def combinationSum3(self, k, n):
        ret = []
        def backtrack(combination, remaining, start):
            if remaining == 0 and len(combination) == k:
                ret.append(combination.copy())
                return
            if remaining < 0 or len(combination) == k:
                return
            for i in range(start, 10):
                combination.append(i)
                backtrack(combination, remaining - i, i + 1)
                combination.pop()
        backtrack([], n, 1)
        return ret