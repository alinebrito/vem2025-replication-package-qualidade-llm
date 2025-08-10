class Solution:
    def subsets(self, nums):
        ret = []
        n = len(nums)
        for i in range(1 << n):
            tmp = []
            for j in range(n):
                if (i >> j) & 1:
                    tmp.append(nums[j])
            ret.append(tmp)
        return ret