class Solution:
    def lastStoneWeight(self, stones):
        while len(stones) > 1:
            stones.sort()
            x = stones.pop()
            y = stones.pop()
            if x != y:
                stones.append(x - y)
        return stones[0] if stones else 0