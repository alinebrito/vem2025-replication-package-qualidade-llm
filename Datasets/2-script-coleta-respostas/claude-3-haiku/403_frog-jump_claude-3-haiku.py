class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] != 1:
            return False
        
        dp = {}
        for stone in stones:
            dp[stone] = set()
        dp[1].add(1)
        
        for stone in stones[:-1]:
            for jump in dp[stone]:
                for nextJump in [jump-1, jump, jump+1]:
                    if nextJump > 0 and stone + nextJump in dp:
                        dp[stone + nextJump].add(nextJump)
        
        return len(dp[stones[-1]]) > 0