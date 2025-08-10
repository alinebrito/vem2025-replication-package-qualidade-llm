class Solution:
    def letterCasePermutation(self, S):
        result = []
        def backtrack(index, path):
            if index == len(S):
                result.append("".join(path))
                return
            if S[index].isalpha():
                path.append(S[index].lower())
                backtrack(index + 1, path)
                path.pop()
                path.append(S[index].upper())
                backtrack(index + 1, path)
                path.pop()
            else:
                path.append(S[index])
                backtrack(index + 1, path)
                path.pop()
        backtrack(0, [])
        return result