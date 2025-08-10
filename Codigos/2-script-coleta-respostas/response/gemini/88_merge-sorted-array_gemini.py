class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        # Two pointers: one starting from the end of nums1 (excluding the zeros)
        # and the other starting from the end of nums2.
        p1 = m - 1
        p2 = n - 1
        
        # Iterate through nums1 from the end
        for i in range(m + n - 1, -1, -1):
            # If p1 is valid and the element at p1 is greater than the element at p2
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[i] = nums1[p1]
                p1 -= 1
            # Otherwise, take the element from nums2
            else:
                nums1[i] = nums2[p2]
                p2 -= 1