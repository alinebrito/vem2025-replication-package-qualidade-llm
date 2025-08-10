class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort(reverse=True)
            x, y = stones[0], stones[1]
            stones = stones[2:]
            if x != y:
                stones.append(x - y)