class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        xor = 0
        for num in nums:
            xor ^= num
        rightmost_set_bit = xor & -xor
        first, second = 0, 0
        for num in nums:
            if num & rightmost_set_bit:
                first ^= num
            else:
                second ^= num
        return [first, second]