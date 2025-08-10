class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        first_max = second_max = -1
        for i, num in enumerate(nums):
            if num > first_max:
                second_max = first_max
                first_max = num
            elif num > second_max:
                second_max = num
        return i if first_max >= 2 * second_max else -1