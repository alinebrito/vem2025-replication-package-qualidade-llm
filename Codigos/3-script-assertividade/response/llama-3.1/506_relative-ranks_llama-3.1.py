class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score = sorted(enumerate(score), key=lambda x: x[1], reverse=True)
        answer = [0] * len(score)
        for i, (idx, _) in enumerate(sorted_score):
            if i == 0:
                answer[idx] = "Gold Medal"
            elif i == 1:
                answer[idx] = "Silver Medal"
            elif i == 2:
                answer[idx] = "Bronze Medal"
            else:
                answer[idx] = str(i + 1)
 return answer