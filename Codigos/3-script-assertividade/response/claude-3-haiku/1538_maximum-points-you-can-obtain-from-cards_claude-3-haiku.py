class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        best = total = sum(cardPoints[:k])
        for i in range(k):
            total = total - cardPoints[k-i-1] + cardPoints[n-i-1]
            best = max(best, total)
        return best