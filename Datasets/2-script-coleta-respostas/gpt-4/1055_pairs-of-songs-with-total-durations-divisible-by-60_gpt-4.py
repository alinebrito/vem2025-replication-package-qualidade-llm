class Solution:
    def numPairsDivisibleBy60(self, time):
        ans, cnt = 0, [0] * 60
        for t in time:
            remainder = t % 60
            ans += cnt[(60 - remainder) % 60]
            cnt[remainder] += 1
        return ans