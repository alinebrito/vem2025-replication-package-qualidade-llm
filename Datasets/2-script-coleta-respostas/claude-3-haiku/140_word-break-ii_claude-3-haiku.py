class Solution:
    def wordBreak(self, s, wordDict):
        dp = [[] for _ in range(len(s) + 1)]
        dp[0] = [""]
        
        for i in range(1, len(s) + 1):
            for j in range(i):
                if s[j:i] in wordDict:
                    for prev in dp[j]:
                        if prev:
                            dp[i].append(prev + " " + s[j:i])
                        else:
                            dp[i].append(s[j:i])
        
        return dp[len(s)]