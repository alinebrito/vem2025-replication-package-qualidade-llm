class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        le = len(A)
        count = 0  
        current = 0  
        for i in range(2, le):
            if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
                current += 1  
                count += current  
            else:
                current = 0  
        return count  