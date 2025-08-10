class Solution:
    def topKFrequent(self, nums, k):
        hs = {}
        for num in nums:
            hs[num] = hs.get(num, 0) + 1
        return sorted(hs, key=hs.get, reverse=True)[:k]