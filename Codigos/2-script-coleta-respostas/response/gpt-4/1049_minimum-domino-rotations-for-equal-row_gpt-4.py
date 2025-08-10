class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        def check(x):
            rotations_a = rotations_b = 0
            for i in range(len(tops)):
                if tops[i] != x and bottoms[i] != x:
                    return float('inf')
                elif tops[i] != x:
                    rotations_a += 1
                elif bottoms[i] != x:
                    rotations_b += 1
            return min(rotations_a, rotations_b)

        result = check(tops[0])
        if tops[0] != bottoms[0]:
            result = min(result, check(bottoms[0]))
        
        return result if result != float('inf') else -1