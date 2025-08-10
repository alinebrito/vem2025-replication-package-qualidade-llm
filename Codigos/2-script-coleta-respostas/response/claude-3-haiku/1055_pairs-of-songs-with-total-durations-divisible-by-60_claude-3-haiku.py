class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        ans, cnt = 0, [0] * 60
        for t in time:
            rem = t % 60
            ans += cnt[(60 - rem) % 60]
            cnt[rem] += 1
        return ans