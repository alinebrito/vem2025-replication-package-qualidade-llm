class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        value = sum(matchsticks)
        n = len(matchsticks)
        if value % 4 != 0:
            return False
        target = value // 4
        matchsticks.sort(reverse=True)
        sides = [0] * 4

        def backtrack(i):
            if i == n:
                return sides[0] == sides[1] == sides[2] == target
            for j in range(4):
                if sides[j] + matchsticks[i] <= target:
                    sides[j] += matchsticks[i]
                    if backtrack(i + 1):
                        return True
                    sides[j] -= matchsticks[i]
            return False

        return backtrack(0)