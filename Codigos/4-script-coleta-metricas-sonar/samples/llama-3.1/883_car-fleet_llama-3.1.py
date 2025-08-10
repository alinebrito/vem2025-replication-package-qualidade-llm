class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = [(target - p) / s for p, s in sorted(zip(position, speed), reverse=True)]
        ans = 1
        prev = time[0]
        for t in time[1:]:
            if t > prev:
                ans += 1
                prev = t
        return ans