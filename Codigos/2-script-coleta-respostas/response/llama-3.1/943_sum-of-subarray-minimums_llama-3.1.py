class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        A = [0] + A
        stack = []
        mod = 10**9 + 7
        total = 0
        for i in range(len(A)):
            while stack and A[stack[-1]] > A[i]:
                j = stack.pop()
                k = stack[-1] if stack else -1
                total += A[j] * (i - j) * (j - k) % mod
                total %= mod
            stack.append(i)
        return total