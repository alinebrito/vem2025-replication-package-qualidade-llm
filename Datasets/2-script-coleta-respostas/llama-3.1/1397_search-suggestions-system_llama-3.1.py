class Solution:
    def suggestedProducts(self, P, S):
        P.sort()
        res = []
        for i in range(len(S)):
            prefix = S[:i+1]
            res.append([p for p in P if p.startswith(prefix)][:3])
        return res