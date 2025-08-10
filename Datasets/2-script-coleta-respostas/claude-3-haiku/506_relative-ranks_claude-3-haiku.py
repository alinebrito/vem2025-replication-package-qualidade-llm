class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        ranks = sorted(score, reverse=True)
        result = []
        for s in score:
            if ranks.index(s) == 0:
                result.append("Gold Medal")
            elif ranks.index(s) == 1:
                result.append("Silver Medal")
            elif ranks.index(s) == 2:
                result.append("Bronze Medal")
            else:
                result.append(str(ranks.index(s) + 1))
        return result