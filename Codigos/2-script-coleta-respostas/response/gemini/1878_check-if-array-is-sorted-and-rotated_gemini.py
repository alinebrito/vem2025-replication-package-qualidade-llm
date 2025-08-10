class Solution:
    def check_rotation(self, nums):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                right -= 1
        pivot = left
        return all(nums[(i + pivot) % len(nums)] <= nums[(i + pivot + 1) % len(nums)] for i in range(len(nums) - 1))