class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        total = len(tops)
        for x in range(1, 7):
            top_rot = bot_rot = 0
            for i in range(total):
                if tops[i] != x and bottoms[i] != x:
                    break
                if tops[i] != x:
                    bot_rot += 1
                if bottoms[i] != x:
                    top_rot += 1
            else:
                return min(top_rot, bot_rot)
        return -1