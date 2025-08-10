class Solution:
    def __init__(self, nums: List[int]):
        self.arr = nums[:]
        self.original = nums[:]

    def reset(self) -> List[int]:
        self.arr = self.original[:]
        return self.arr

    def shuffle(self) -> List[int]:
        n = len(self.arr)
        for i in range(n):
            j = random.randint(i, n - 1)
            self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
        return self.arr