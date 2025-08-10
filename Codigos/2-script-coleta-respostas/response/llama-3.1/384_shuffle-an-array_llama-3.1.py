class Solution:
import random

class Solution:
    def __init__(self, nums: List[int]):
        self.original = nums[:]
        self.arr = nums[:]

    def reset(self) -> List[int]:
        self.arr = self.original[:]
        return self.arr

    def shuffle(self) -> List[int]:
        random.shuffle(self.arr)
        return self.arr