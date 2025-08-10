class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        value = sum(matchsticks)
        if value % 4 != 0:
            return False  
        side = value // 4  
        matchsticks.sort(reverse=True)

        def can_form_square(index, sides):
            if index == len(matchsticks):
                return all(side == 0 for side in sides)
            for i in range(4):
                if sides[i] + matchsticks[index] <= side:
                    sides[i] += matchsticks[index]
                    if can_form_square(index + 1, sides):
                        return True  
                    sides[i] -= matchsticks[index]
                if sides[i] == 0:
                    break  
            return False

        return can_form_square(0, [0] * 4)