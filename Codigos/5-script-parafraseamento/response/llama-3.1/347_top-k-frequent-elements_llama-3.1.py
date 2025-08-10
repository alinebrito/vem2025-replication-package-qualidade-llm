class Solution:
    def topKFrequent(self, nums, k):
        hs = {}
        for num in nums:
            if num in hs:
                hs[num] += 1
            else:
                hs[num] = 1
        sorted_hs = sorted(hs.items(), key=lambda x: x[1], reverse=True)
        return [x[0] for x in sorted_hs[:k]], [x[1] for x in sorted_hs[:k]]