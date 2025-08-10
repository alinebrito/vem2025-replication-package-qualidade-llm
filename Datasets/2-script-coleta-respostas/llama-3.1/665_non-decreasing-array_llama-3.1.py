class Solution:
    def checkPossibility(self, nums: list[int]) -> bool:
        err = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                err += 1
                if err > 1:
                    return False
        return True