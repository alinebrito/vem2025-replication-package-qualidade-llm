class Solution:
    def __init__(self, nums: List[int]):
        self.original = nums[:]
        self.arr = nums[:]
    
    def reset(self) -> List[int]:
        self.arr = self.original[:]
        return self.arr
    
    def shuffle(self) -> List[int]:
        for i in range(len(self.arr)):
            j = random.randint(i, len(self.arr) - 1)
            self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
        return self.arr