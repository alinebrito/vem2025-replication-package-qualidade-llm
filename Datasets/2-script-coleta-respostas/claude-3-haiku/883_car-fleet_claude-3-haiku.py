class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        times = [float(target - p) / s for p, s in cars]
        ans = 1 if times else 0
        for i in range(1, len(times)):
            if times[i] > times[i-1]:
                ans += 1
        return ans