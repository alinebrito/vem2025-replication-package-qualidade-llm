class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * (n + 1) for _ in range(n + 1)]
        count = 0
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if i == j:
                    dp[i][j] = True
                elif i + 1 == j:
                    dp[i][j] = s[i] == s[j]
                else:
                    dp[i][j] = s[i] == s[j] and dp[i + 1][j - 1]
                if dp[i][j]:
                    count += 1
        return count