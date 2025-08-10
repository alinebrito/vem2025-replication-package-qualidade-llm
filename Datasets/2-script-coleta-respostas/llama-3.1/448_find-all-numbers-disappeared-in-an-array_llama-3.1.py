class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i, num in enumerate(nums):
            while 1 <= num <= n and nums[num - 1] != num:
                nums[num - 1], nums[i] = nums[i], nums[num - 1]
        return [i + 1 for i, num in enumerate(nums) if num != i + 1]