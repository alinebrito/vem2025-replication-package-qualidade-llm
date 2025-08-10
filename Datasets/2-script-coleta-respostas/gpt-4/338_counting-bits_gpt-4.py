class Solution:
    def countBits(self, num: int) -> List[int]:
        counter = [0] * (num + 1)
        for i in range(1, num + 1):
            counter[i] = counter[i >> 1] + (i & 1)
        return counter