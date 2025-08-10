class Solution:
    def divisorGame(self, N: int) -> bool:
        dp = [False for i in range(N+1)]