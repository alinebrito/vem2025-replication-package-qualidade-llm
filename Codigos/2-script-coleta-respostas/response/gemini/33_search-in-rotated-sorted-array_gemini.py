class Solution:
    def search(self, nums, target):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # Determine if the left half is sorted
            if nums[left] <= nums[mid]:
                # If target is within the sorted left half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                # Otherwise, target is in the unsorted right half
                else:
                    left = mid + 1
            # If the right half is sorted
            else:
                # If target is within the sorted right half
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                # Otherwise, target is in the unsorted left half
                else:
                    right = mid - 1

        return -1