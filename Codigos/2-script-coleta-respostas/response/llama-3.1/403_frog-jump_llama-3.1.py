class Solution:
    def canCross(self, stones: list[int]) -> bool:
        n = len(stones)
        stone_set = set(stones)
        def dfs(stone, jump):
            if stone == stones[-1]:
                return True
            if jump < 1 or stone + jump not in stone_set:
                return False
            return dfs(stone + jump, jump) or dfs(stone + jump, jump - 1) or dfs(stone + jump, jump + 1)
        return dfs(stones[0], 1)