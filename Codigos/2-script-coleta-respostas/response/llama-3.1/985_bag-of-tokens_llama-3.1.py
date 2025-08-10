class Solution(object):
    def bagOfTokensScore(self, tokens, power):
        tokens.sort()
        score = 0
        max_score = 0
        left, right = 0, len(tokens) - 1
        while left <= right:
            if tokens[left] <= power:
                power -= tokens[left]
                score += 1
                left += 1
            elif score > 0:
                power += tokens[right]
                score -= 1
                right -= 1
            else:
                break
            max_score = max(max_score, score)
        return max_score