class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        total = len(tops)
        for x in range(1, 7):
            top_rotations = bottom_rotations = 0
            for i in range(total):
                if tops[i] != x and bottoms[i] != x:
                    break
                if tops[i] != x:
                    top_rotations += 1
                if bottoms[i] != x:
                    bottom_rotations += 1
            else:
                return min(top_rotations, bottom_rotations)
        return -1