class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        A = [0] + A  
        stack = []
        total_sum = 0  
        mod = 10**9 + 7
        
        for i in range(len(A)):
            while stack and A[stack[-1]] > A[i]:
                j = stack.pop()
                k = stack[-1] if stack else -1  
                total_sum += A[j] * (i - j) * (j - k)
                total_sum %= mod  
            stack.append(i)
        
        return total_sum  