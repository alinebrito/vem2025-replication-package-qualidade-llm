class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        total = sum(cardPoints[:k])
        best = total
        for i in range(k, n):
            total = total - cardPoints[i - k] + cardPoints[i]
            best = max(best, total)
        return best