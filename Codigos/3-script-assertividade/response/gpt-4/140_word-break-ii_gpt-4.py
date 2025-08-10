class Solution:
    def wordBreak(self, s, wordDict):
        def backtrack(start):
            if start in memo:
                return memo[start]
            result = []
            if start == len(s):
                return [""]

            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in wordDict:
                    for sub in backtrack(end):
                        if sub:
                            result.append(word + " " + sub)
                        else:
                            result.append(word)
            memo[start] = result
            return result

        memo = {}
        return backtrack(0)