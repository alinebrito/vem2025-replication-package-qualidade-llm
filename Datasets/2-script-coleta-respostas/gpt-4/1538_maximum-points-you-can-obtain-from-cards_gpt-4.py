class Solution:
    def maxScore(self, C: List[int], K: int) -> int:
        best = total = sum(C[:K])
        n = len(C)
        for i in range(K):
            total = total - C[K - 1 - i] + C[n - 1 - i]
            best = max(best, total)
        return best