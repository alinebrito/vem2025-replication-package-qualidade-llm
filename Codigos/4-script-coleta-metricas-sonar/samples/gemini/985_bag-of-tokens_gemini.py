class Solution(object):
    def bagOfTokensScore(self, tokens, power):
        tokens.sort()
        l, r = 0, len(tokens) - 1
        score = 0
        ans = 0
        while l <= r:
            if power >= tokens[l]:
                power -= tokens[l]
                score += 1
                l += 1
                ans = max(ans, score)
            elif score >= 1 and l < r:
                power += tokens[r]
                score -= 1
                r -= 1
            else:
                break
        return ans 