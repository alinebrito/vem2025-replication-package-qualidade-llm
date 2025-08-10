class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        n, hm, res = len(nums1), {}, 0
        for i in range(n):
            for j in range(n):
                hm[nums1[i] + nums2[j]] = hm.get(nums1[i] + nums2[j], 0) + 1
        for i in range(n):
            for j in range(n):
                res += hm.get(-(nums3[i] + nums4[j]), 0)
        return res