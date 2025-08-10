class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        first_max = second_max = -1
        max_index = -1
        for i, num in enumerate(nums):
            if num > first_max:
                second_max = first_max
                first_max = num
                max_index = i
            elif num > second_max:
                second_max = num