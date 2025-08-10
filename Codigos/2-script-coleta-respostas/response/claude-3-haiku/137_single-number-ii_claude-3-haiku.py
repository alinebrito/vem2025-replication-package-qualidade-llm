class Solution:
    def singleNumber(self, nums):
        result = 0
        for i in range(32):
            bit_sum = 0
            for num in nums:
                if (num >> i) & 1:
                    bit_sum += 1
            result |= (bit_sum % 3) << i
        return result if result <= 0x7FFFFFFF else result | ~0xFFFFFFFF