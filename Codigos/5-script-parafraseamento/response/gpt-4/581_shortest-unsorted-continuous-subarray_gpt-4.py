class Solution:
    def findUnsortedSubarray(self, N: List[int]) -> int:
        lenN, left, right = len(N) - 1, -1, -1  
        sortedN = sorted(N)
        for i in range(lenN + 1):
            if N[i] != sortedN[i]:
                if left == -1:
                    left = i  
                right = i  
        return 0 if left == -1 else right - left + 1  