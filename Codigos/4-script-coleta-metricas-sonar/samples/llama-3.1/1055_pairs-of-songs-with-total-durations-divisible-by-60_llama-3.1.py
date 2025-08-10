class Solution:
    def numPairsDivisibleBy60(self, time):
        ans, cnt = 0, [0] * 60
        for t in time:
            ans += cnt[(60 - t % 60) % 60]
            cnt[t % 60] += 1
        return ans