class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ans = prev = 0
        for t, s in sorted(zip([target - p for p in position], speed), reverse=True):
            if not prev or t / s > prev:
                ans += 1
                prev = t / s
        return ans