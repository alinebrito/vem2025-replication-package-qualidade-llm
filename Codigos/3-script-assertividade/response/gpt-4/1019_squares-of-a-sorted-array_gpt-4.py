class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        n = len(A)
        result = [0] * n  
        left, right = 0, n - 1  
        for i in range(n - 1, -1, -1):
            if abs(A[left]) > abs(A[right]):
                result[i] = A[left] * A[left]
                left += 1  
            else:
                result[i] = A[right] * A[right]
                right -= 1  
        return result  