class Solution:
    def subsetsWithDup(self, S):
        res = [[]]
        S.sort()
        for num in S:
            temp = [subset + [num] for subset in res if subset + [num] not in res]
            res.extend(temp)