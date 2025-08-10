class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        total = len(tops)
        for target in [tops[0], bottoms[0]]:
            top_rotations = bottom_rotations = 0
            for i in range(total):
                if tops[i] != target and bottoms[i] != target:
                    break
                elif tops[i] != target:
                    top_rotations += 1
                elif bottoms[i] != target:
                    bottom_rotations += 1
            else:
                return total - max(top_rotations, bottom_rotations)