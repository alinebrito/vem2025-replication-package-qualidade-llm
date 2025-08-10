class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        n, hm, res = len(nums1), defaultdict(int), 0
        for a in nums1:
            for b in nums2:
                hm[a + b] += 1
        for c in nums3:
            for d in nums4:
                res += hm[-(c + d)]
        return res