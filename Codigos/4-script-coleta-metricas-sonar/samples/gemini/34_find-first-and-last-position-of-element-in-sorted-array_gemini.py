class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearch(nums, target, left, right):
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1

        start = binarySearch(nums, target, 0, len(nums) - 1)
        if start == -1:
            return [-1, -1]

        end = start
        while end < len(nums) - 1 and nums[end + 1] == target:
            end += 1

        return [start, end]