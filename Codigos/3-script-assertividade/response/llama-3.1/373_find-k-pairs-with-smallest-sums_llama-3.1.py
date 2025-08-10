class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        queue = []
        if nums1 and nums2:
            queue.append((nums1[0] + nums2[0], 0, 0))
        res = []
        while queue and len(res) < k:
            _, i, j = queue.pop(0)
            res.append([nums1[i], nums2[j]])
            if i + 1 < len(nums1):
                queue.append((nums1[i + 1] + nums2[j], i + 1, j))
            if j + 1 < len(nums2) and (not queue or nums1[i] + nums2[j + 1] < queue[0][0]):
                queue.append((nums1[i] + nums2[j + 1], i, j + 1))
        return res