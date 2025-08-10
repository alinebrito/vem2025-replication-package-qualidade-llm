class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        result = []
        for i in range(min(k, len(nums1))):
            result.append([nums1[i], nums2[0]])
        left, right = 1, 0
        while len(result) < k and (left < len(nums1) or right < len(nums2)):
            if left < len(nums1) and (right >= len(nums2) or nums1[left] + nums2[right] <= nums1[left-1] + nums2[right]):
                result.append([nums1[left], nums2[0]])
                left += 1
            else:
                result.append([nums1[0], nums2[right]])
                right += 1
        return result[:k]