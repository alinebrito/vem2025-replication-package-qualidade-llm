class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        result = []
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2) and len(result) < k:
            result.append([nums1[i], nums2[j]])
            if sum([nums1[i], nums2[j]]) < sum([nums1[i], nums2[j+1]]):
                i += 1
            else:
                j += 1
        return result