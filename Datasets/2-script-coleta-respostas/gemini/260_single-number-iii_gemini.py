class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        n = len(nums)
        xor = 0
        for i in range(n):
            xor ^= nums[i]
        diff = xor & -xor
        res = [0, 0]
        for i in range(n):
            if (nums[i] & diff) == 0:
                res[0] ^= nums[i]
            else:
                res[1] ^= nums[i]
        return res