class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        value = sum(matchsticks)
        if value % 4 != 0:
            return False
        target = value // 4
        matchsticks.sort(reverse=True)
        sides = [0] * 4
        return self.backtrack(matchsticks, 0, sides, target)

    def backtrack(self, matchsticks: List[int], index: int, sides: List[int], target: int) -> bool:
        if index == len(matchsticks):
            return True
        for i in range(4):
            if sides[i] + matchsticks[index] <= target:
                sides[i] += matchsticks[index]
                if self.backtrack(matchsticks, index + 1, sides, target):
                    return True
                sides[i] -= matchsticks[index]
        return False