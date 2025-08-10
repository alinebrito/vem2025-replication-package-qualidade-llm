class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        num_bits = len(bin(n)) - 2
        return n ^ ((1 << num_bits) - 1)