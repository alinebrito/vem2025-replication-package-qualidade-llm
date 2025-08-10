class Solution:
    def reversePairs(self, nums):
        def mergeSort(nums):
            if len(nums) <= 1:
                return nums, 0
            mid = len(nums) // 2
            left, leftInv = mergeSort(nums[:mid])
            right, rightInv = mergeSort(nums[mid:])
            merged, mergedInv = merge(left, right)
            return merged, leftInv + rightInv + mergedInv

        def merge(left, right):
            merged = []
            invCount = 0
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    invCount += len(left) - i
                    j += 1
            merged.extend(left[i:])
            merged.extend(right[j:])
            return merged, invCount

        _, invCount = mergeSort(nums)