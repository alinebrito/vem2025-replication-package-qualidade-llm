class Solution:
    def wordBreak(self, s, wordDict):
        def backtrack(start, path):
            if start == len(s):
                res.append(' '.join(path))
                return
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in wordDict:
                    backtrack(end, path + [word])

        res = []
        backtrack(0, [])
        return res