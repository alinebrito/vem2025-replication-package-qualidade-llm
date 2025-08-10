class Solution:
    def wordBreak(self, s, wordDict):
        res = []
        def dfs(i, cur):
            if i == len(s):
                res.append(" ".join(cur))
                return
            for j in range(i + 1, len(s) + 1):
                if s[i:j] in wordDict:
                    dfs(j, cur + [s[i:j]])
        dfs(0, [])
        return res