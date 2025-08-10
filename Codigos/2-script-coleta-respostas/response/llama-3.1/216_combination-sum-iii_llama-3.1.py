class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(start, path, remain):
            if len(path) == k:
                if remain == 0:
                    ret.append(path)
                return
            for i in range(start, 10):
                if i > remain:
                    break
                backtrack(i + 1, path + [i], remain - i)

        ret = []
        backtrack(1, [], n)
        return ret