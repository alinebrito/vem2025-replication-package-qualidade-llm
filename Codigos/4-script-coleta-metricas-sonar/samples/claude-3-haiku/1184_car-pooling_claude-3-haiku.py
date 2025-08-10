class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        counts = [0] * 1001
        for trip in trips:
            num_passengers, from_loc, to_loc = trip
            for i in range(from_loc, to_loc):
                counts[i] += num_passengers
                if counts[i] > capacity:
                    return False
        return True