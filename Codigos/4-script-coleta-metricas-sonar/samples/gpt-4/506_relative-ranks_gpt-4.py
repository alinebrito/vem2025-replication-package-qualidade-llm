class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score = sorted(score, reverse=True)
        ranks = ["Gold Medal", "Silver Medal", "Bronze Medal"] + [str(i) for i in range(4, len(score) + 1)]
        rank_dict = {score: ranks[i] for i, score in enumerate(sorted_score)}
        return [rank_dict[score] for score in score]