class Solution:
    def __init__(self, nums: List[int]):
        self.arr = nums[:]

    def reset(self) -> List[int]:
        return self.arr

    def shuffle(self) -> List[int]:
        import random
        arr = self.arr[:]
        random.shuffle(arr)
        return arr