class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        dp = [0] * len(envelopes)
        res = 0
        for i in range(len(envelopes)):
            for j in range(i):
                if envelopes[i][1] > envelopes[j][1] and dp[i] < dp[j]:
                    dp[i] = dp[j]
            dp[i] += 1
            res = max(res, dp[i])
        return res