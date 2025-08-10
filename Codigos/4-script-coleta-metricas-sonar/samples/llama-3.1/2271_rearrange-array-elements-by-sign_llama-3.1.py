class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos, neg = [], []
 for num in nums:
            if num > 0:
                pos.append(num)
            else:
                neg.append(num)
        res = []
        for p, n in zip(pos, neg):
            res.append(p)
            res.append(n)
        return res