class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        min_heap = []
        for i in range(min(k, len(nums1))):
            min_heap.append((nums1[i] + nums2[0], i, 0))
        result = []
        while k > 0 and min_heap:
            sum_val, i, j = min_heap.pop(0)
            result.append([nums1[i], nums2[j]])
            if j + 1 < len(nums2):
                min_heap.append((nums1[i] + nums2[j + 1], i, j + 1))
            min_heap.sort()
            k -= 1  
        return result  