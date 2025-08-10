class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(set(nums)) >= 3:
            return sorted(set(nums), reverse=True)[2]
        else:
            return max(nums)