class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp = sorted(nums)
        result = []
        for num in nums:
            result.append(temp.index(num))
        return result