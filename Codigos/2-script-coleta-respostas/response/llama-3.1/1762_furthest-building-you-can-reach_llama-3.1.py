class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        bricks_used = 0
        ladders_used = 0
        for i in range(1, len(heights)):
            if heights[i] <= heights[i - 1]:
                continue
            elif ladders_used > 0:
                ladders_used -= 1
            else:
                bricks_used += heights[i] - heights[i - 1]
                if bricks_used > bricks:
                    return i - 1
        return len(heights) - 1