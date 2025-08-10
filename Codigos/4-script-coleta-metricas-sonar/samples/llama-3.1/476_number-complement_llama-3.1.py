class Solution:
    def findComplement(self, num: int) -> int:
        mask = (1 << 31) - 1  # Create a mask with 31 ones
        while num & mask == 0:
            mask >>= 1
        return num ^ mask