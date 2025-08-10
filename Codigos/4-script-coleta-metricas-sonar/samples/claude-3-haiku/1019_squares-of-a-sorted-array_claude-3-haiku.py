class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        left, right = 0, len(A) - 1
        result = [0] * len(A)
        
        for i in range(len(A) - 1, -1, -1):
            if abs(A[left]) > abs(A[right]):
                result[i] = A[left] ** 2
                left += 1
            else:
                result[i] = A[right] ** 2
                right -= 1
        
        return result