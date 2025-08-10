class Solution:
    def maxArea(self, h: int, w: int, hc: List[int], vc: List[int]) -> int:
        hc.sort()
        vc.sort()
        mxh = max(hc[0], h - hc[-1])
        mxv = max(vc[0], w - vc[-1])
        for i in range(1, len(hc)):
            mxh = max(mxh, hc[i] - hc[i-1])
        for i in range(1, len(vc)):
            mxv = max(mxv, vc[i] - vc[i-1])
        return (mxh * mxv) % (10**9 + 7)