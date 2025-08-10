class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        res = []
        for num1 in nums1:
            for num2 in nums2:
                res.append([num1, num2])
                if len(res) == k:
                    return res
        res.sort(key=lambda x: x[0] + x[1])
        return res[:k]