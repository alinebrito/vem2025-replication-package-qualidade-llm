class Solution:
    def topKFrequent(self, nums, k):
        hs = {}
        for num in nums:
            if num in hs:
                hs[num] += 1
            else:
                hs[num] = 1
        freq = sorted(hs.items(), key=lambda x: x[1], reverse=True)
        res_num = [x[0] for x in freq[:k]]
        res_freq = [x[1] for x in freq[:k]]
        return res_num, res_freq