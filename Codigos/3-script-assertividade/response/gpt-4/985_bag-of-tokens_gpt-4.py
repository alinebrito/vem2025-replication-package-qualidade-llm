class Solution(object):
    def bagOfTokensScore(self, tokens, power):
        tokens.sort()
        score = maxScore = 0
        left, right = 0, len(tokens) - 1
        
        while left <= right:
            if power >= tokens[left]:
                power -= tokens[left]
                left += 1
                score += 1
                maxScore = max(maxScore, score)
            elif score > 0:
                power += tokens[right]
                right -= 1
                score -= 1
            else:
                break
        
        return maxScore