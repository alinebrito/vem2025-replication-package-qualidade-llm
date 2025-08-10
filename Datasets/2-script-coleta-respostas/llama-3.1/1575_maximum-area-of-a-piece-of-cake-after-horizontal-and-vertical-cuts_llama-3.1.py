class Solution:
    def maxArea(self, h: int, w: int, hc: list[int], vc: list[int]) -> int:
        hc.sort()
        vc.sort()
        max_h = max(hc)
        max_v = max(vc)
        max_h = max(max_h, h - hc[-1])
        max_v = max(max_v, w - vc[-1])
        return (max_h * max_v) % (10**9 + 7)