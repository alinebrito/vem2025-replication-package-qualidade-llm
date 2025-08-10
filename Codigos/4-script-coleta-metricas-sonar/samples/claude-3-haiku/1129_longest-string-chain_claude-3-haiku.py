class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        dp = {}
        res = 0
        for word in words:
            dp[word] = 1
            for i in range(len(word)):
                prev = word[:i] + word[i+1:]
                if prev in dp:
                    dp[word] = max(dp[word], dp[prev] + 1)
            res = max(res, dp[word])
        return res