class Solution:
    def maxEnvelopes(self, E: List[List[int]]) -> int:
        E.sort(key=lambda x: (x[0], -x[1]))
        dp = []
        for _, h in E:
            i = bisect.bisect_left(dp, h)
            if i == len(dp):
                dp.append(h)
            else:
                dp[i] = h  
        return len(dp)