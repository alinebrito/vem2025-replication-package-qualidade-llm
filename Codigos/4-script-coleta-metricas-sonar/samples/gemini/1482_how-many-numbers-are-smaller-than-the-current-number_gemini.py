class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp = sorted(nums)
        result = []
        for i in nums:
            result.append(temp.index(i))
        return result