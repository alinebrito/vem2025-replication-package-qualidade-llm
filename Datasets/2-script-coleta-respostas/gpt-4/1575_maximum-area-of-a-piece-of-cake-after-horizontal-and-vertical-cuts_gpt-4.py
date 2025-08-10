class Solution:
    def maxArea(self, h: int, w: int, hc: List[int], vc: List[int]) -> int:
        hc.sort()
        vc.sort()
        max_h = max(hc[0], h - hc[-1]) if hc else h  
        max_w = max(vc[0], w - vc[-1]) if vc else w  
        for i in range(1, len(hc)):
            max_h = max(max_h, hc[i] - hc[i - 1])
        for i in range(1, len(vc)):
            max_w = max(max_w, vc[i] - vc[i - 1])
        return (max_h * max_w) % (10**9 + 7)