class Solution:
    def reversePairs(self, nums):
        def merge_sort(left, right):
            if left >= right:
                return 0
            mid = (left + right) // 2
            count = merge_sort(left, mid) + merge_sort(mid + 1, right)
            i, j = mid, right
            while i >= left:
                while j > mid and nums[i] > 2 * nums[j]:
                    j -= 1
                count += j - mid
                i -= 1
            nums[left:right + 1] = sorted(nums[left:right + 1])
            return count
        return merge_sort(0, len(nums) - 1)