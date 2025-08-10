class Solution:
    def suggestedProducts(self, P: List[str], S: str) -> List[List[str]]:
        P.sort()
        res, prefix, i = [], '', 0
        for c in S:
            prefix += c
            i = bisect.bisect_left(P, prefix, i)
            res.append([w for w in P[i:i + 3] if w.startswith(prefix)])
        return res