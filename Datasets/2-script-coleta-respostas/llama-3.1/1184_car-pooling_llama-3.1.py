class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        count = [0] * 1001
        for numPassengers, from_i, to_i in trips:
            count[from_i] += numPassengers
            count[to_i] -= numPassengers
        current_passengers = 0
        for c in count:
            current_passengers += c
            if current_passengers > capacity:
                return False
        return True