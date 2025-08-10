class Solution:
    def topKFrequent(self, nums, k):
        hs = {}
        for num in nums:
            hs[num] = hs.get(num, 0) + 1
        return [x[0] for x in sorted(hs.items(), key=lambda x: x[1], reverse=True)[:k]]