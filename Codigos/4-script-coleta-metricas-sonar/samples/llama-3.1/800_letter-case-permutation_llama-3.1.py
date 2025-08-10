class Solution:
    def letterCasePermutation(self, S):
        def backtrack(sub, idx):
            if idx == len(S):
                res.append(sub)
                return
            if S[idx].isalpha():
                backtrack(sub + S[idx].lower(), idx + 1)
                backtrack(sub + S[idx].upper(), idx + 1)
            else:
                backtrack(sub + S[idx], idx + 1)
        
        res = []
        backtrack("", 0)
        return res