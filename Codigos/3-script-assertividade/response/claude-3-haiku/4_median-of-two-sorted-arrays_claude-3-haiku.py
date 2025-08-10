class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m
        
        left, right = 0, m
        while left <= right:
            partitionX = (left + right) // 2
            partitionY = (m + n + 1) // 2 - partitionX
            
            maxLeftX = nums1[partitionX - 1] if partitionX != 0 else float('-inf')
            minRightX = nums1[partitionX] if partitionX != m else float('inf')
            
            maxLeftY = nums2[partitionY - 1] if partitionY != 0 else float('-inf')
            minRightY = nums2[partitionY] if partitionY != n else float('inf')
            
            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                if (m + n) % 2 == 0:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
                else:
                    return max(maxLeftX, maxLeftY)
            elif maxLeftX > minRightY:
                right = partitionX - 1
            else:
                left = partitionX + 1