class Solution:
    def subsetsWithDup(self, nums):
        res = [[]]
        nums.sort()
        for num in nums:
            new_sets = [subset + [num] for subset in res if not (subset and subset[-1] == num)]
            res.extend(new_sets)
        return res