class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        A = [0]+A
        n = len(A)
        left, right = [0] * n, [0] * n
        stack = []
        for i in range(n):
            while stack and A[stack[-1]] >= A[i]:
                stack.pop()
            left[i] = i - stack[-1] if stack else i + 1
            stack.append(i)
        stack = []
        for i in range(n-1, -1, -1):
            while stack and A[stack[-1]] > A[i]:
                stack.pop()
            right[i] = stack[-1] - i if stack else n - i
            stack.append(i)
        return sum(A[i] * left[i] * right[i] for i in range(n)) % (10 ** 9 + 7)