class Solution:
    def divisorGame(self, N: int) -> bool:
        dp = [False for i in range(N+1)]
        for i in range(2, N+1):
            for x in range(1, i):
                if i % x == 0:
                    dp[i] = dp[i] or not dp[i-x]
        return dp[N]