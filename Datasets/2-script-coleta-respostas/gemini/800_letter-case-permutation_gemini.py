class Solution:
    def letterCasePermutation(self, S):
        res = [""]
        for c in S:
            if c.isalpha():
                res = [i + j for i in res for j in [c.upper(), c.lower()]]
            else:
                res = [i + c for i in res]
        return res