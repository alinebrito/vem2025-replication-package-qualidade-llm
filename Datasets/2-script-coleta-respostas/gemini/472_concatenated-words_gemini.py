class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        wordset = set(words)
        res = []
        for word in words:
            n = len(word)
            dp = [False] * (n + 1)
            dp[0] = True
            for i in range(1, n + 1):
                for j in range(i):
                    if dp[j] and word[j:i] in wordset:
                        dp[i] = True
                        break
            if dp[-1] and len(word.split()) > 1:
                res.append(word)
        return res 