class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        A = [0] + A
        n = len(A)
        mod = 10**9 + 7
        stack = []
        result = 0
        for i in range(n):
            while stack and A[stack[-1]] > A[i]:
                j = stack.pop()
                k = stack[-1] if stack else -1
                result += A[j] * (i - j) * (j - k)
                result %= mod
            stack.append(i)
        return result