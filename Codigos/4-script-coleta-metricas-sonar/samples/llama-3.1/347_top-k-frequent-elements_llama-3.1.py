class Solution:
    def topKFrequent(self, nums, k):
        hs = {}
        for n in nums:
            if n in hs:
                hs[n] += 1
            else:
                hs[n] = 1
        res = sorted(hs, key=hs.get, reverse=True)