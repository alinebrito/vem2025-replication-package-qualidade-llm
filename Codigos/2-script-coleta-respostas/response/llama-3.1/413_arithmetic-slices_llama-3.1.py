class Solution:
    def numberOfArithmeticSlices(self, A):
        le = len(A)
        dp = [0] * le
        ans = 0
        for i in range(2, le):
            if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
                dp[i] = dp[i - 1] + 1
                ans += dp[i]
        return ans