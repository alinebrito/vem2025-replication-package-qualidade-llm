class Solution:
    def maxArea(self, h: int, w: int, hc: List[int], vc: List[int]) -> int:
        hc.sort()
        vc.sort()
        max_h = max(hc[i] - hc[i - 1] for i in range(1, len(hc)))
        max_h = max(max_h, hc[0], h - hc[-1])
        max_v = max(vc[i] - vc[i - 1] for i in range(1, len(vc)))
        max_v = max(max_v, vc[0], w - vc[-1])
        return (max_h * max_v) % (10**9 + 7)