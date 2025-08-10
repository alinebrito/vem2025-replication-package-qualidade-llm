class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        le=len(A)
        if le<3:
            return 0
        dp=[0]*le
        for i in range(2,le):
            if A[i]-A[i-1]==A[i-1]-A[i-2]:
                dp[i]=dp[i-1]+1
        return sum(dp)