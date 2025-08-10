class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = [(target - p) / s for p, s in sorted(zip(position, speed))]
        fleets = 0
        prev_time = 0
        for t in reversed(time):
            if t > prev_time:
                fleets += 1
                prev_time = t
        return fleets