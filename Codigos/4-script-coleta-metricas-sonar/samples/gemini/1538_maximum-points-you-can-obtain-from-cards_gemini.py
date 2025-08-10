class Solution:
    def maxScore(self, C: List[int], K: int) -> int:
        best = total = sum(C[:K])
        for i in range(K - 1, -1, -1):
            total += C[len(C) - (K - i)] - C[i]
            best = max(best, total)
        return best