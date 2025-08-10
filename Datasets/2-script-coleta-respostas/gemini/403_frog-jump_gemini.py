class Solution:
    def canCross(self, stones: List[int]) -> bool:
        dp = {}
        for i in range(len(stones)):
            dp[stones[i]] = set()
        dp[stones[0]].add(0)
        for i in range(len(stones)):
            for k in dp[stones[i]]:
                for step in [k - 1, k, k + 1]:
                    if step > 0 and stones[i] + step in dp:
                        dp[stones[i] + step].add(step)
        return len(dp[stones[-1]]) > 0