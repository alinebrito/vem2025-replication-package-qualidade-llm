class Solution:
    def reversePairs(self, nums):
        def mergeSort(left, right):
            if left >= right:
                return 0
            mid = (left + right) // 2
            res = mergeSort(left, mid) + mergeSort(mid + 1, right)
            i = left
            j = mid + 1
            k = left
            while i <= mid and j <= right:
                if nums[i] > 2 * nums[j]:
                    res += mid - i + 1
                    nums[k] = nums[i]
                    i += 1
                else:
                    nums[k] = nums[j]
                    j += 1
                k += 1
            while i <= mid:
                nums[k] = nums[i]
                i += 1
                k += 1
            while j <= right:
                nums[k] = nums[j]
                j += 1
                k += 1
            return res

        return mergeSort(0, len(nums) - 1)