class Solution:
    def combinationSum3(self, k, n):
        ret = []
        def backtrack(start, path, remaining, k):
            if remaining == 0 and len(path) == k:
                ret.append(path)
                return
            for i in range(start, 10):
                if i > remaining:
                    break
                backtrack(i + 1, path + [i], remaining - i, k)
        backtrack(1, [], n, k)
        return ret