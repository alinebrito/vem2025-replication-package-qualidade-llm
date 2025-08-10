class Solution:
    def reversePairs(self, nums):
        self.cnt = 0
        def merge(left, right):
            l, r = 0, 0
            while l < len(left) and r < len(right):
                if left[l] <= 2 * right[r]:
                    l += 1
                else:
                    self.cnt += len(left) - l
                    r += 1
            return sorted(left+right)
        
        def mergeSort(nums):
            if len(nums) <= 1:
                return nums
            mid = len(nums)//2
            left = mergeSort(nums[:mid])
            right = mergeSort(nums[mid:])
            return merge(left, right)
        
        mergeSort(nums)
        return self.cnt