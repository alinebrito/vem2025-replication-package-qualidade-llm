class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        m, n = len(nums1), len(nums2)
        total = m + n
        if total % 2 == 1:
            return self.findKth(nums1, 0, m - 1, nums2, 0, n - 1, (total + 1) // 2)
        else:
            return (self.findKth(nums1, 0, m - 1, nums2, 0, n - 1, total // 2) +
                    self.findKth(nums1, 0, m - 1, nums2, 0, n - 1, total // 2 + 1)) / 2

    def findKth(self, nums1, i, m, nums2, j, n, k):
        if m > n:
            return self.findKth(nums2, j, n, nums1, i, m, k)
        if m == 0:
            return nums2[j + k - 1]
        if k == 1:
            return min(nums1[i], nums2[j])
        
        midVal1 = min(m, k // 2)
        midVal2 = k - midVal1
        
        if nums1[i + midVal1 - 1] <= nums2[j + midVal2 - 1]:
            return self.findKth(nums1, i + midVal1, m, nums2, j, n, k - midVal1)
        else:
            return self.findKth(nums1, i, m, nums2, j + midVal2, n, k - midVal2)