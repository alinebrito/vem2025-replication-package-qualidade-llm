class Solution:
    def intersect(self, nums1, nums2):
        result = []
        count1 = {}
        count2 = {}
        
        for num in nums1:
            count1[num] = count1.get(num, 0) + 1
        
        for num in nums2:
            count2[num] = count2.get(num, 0) + 1
        
        for num in set(nums1) & set(nums2):
            result.extend([num] * min(count1[num], count2[num]))
        
        return result