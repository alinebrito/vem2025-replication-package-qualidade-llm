class Solution:
    def moveZeroes(self, nums: list) -> None:
        slow = 0

        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1

        while slow < len(nums):
            nums[slow] = 0
            slow += 1