class Solution:
    def intersect(self, nums1, nums2):
        intersection = []
        for num in nums1:
            if num in nums2:
                intersection.append(num)
                nums2.remove(num)
        return intersection