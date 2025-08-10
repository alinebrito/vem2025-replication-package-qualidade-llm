class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])
        curr = float('-inf')
        ans = 0
        for c, d in pairs:
            if curr < c:
                curr = d
                ans += 1
        return ans