class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        A = [0] + A
        stack = []
        result = 0
        mod = 10**9 + 7
        for i in range(len(A)):
            while stack and A[stack[-1]] > A[i]:
                j = stack.pop()
                k = stack[-1] if stack else -1
                result += A[j] * (i - j) * (j - k)
                result %= mod
            stack.append(i)
        return result