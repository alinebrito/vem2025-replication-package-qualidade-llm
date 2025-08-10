class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        total = len(tops)
        for i in range(1, 7):
            top_count = 0
            bottom_count = 0
            for j in range(total):
                if tops[j] == i:
                    top_count += 1
                if bottoms[j] == i:
                    bottom_count += 1
                if top_count == total or bottom_count == total:
                    return total - max(top_count, bottom_count)
        return -1