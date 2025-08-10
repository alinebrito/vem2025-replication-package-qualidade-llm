class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        count = [0] * 1001
        for trip in trips:
            count[trip[1]] += trip[0]
            count[trip[2]] -= trip[0]
        for c in count:
            capacity -= c
            if capacity < 0:
                return False
        return True