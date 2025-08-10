class Solution:
    def __init__(self):
        self.nums = []
        self.index_map = {}

    def insert(self, val: int) -> bool:
        if val in self.index_map:
            return False
        self.nums.append(val)
        self.index_map[val] = len(self.nums) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.index_map:
            return False
        last_num, last_index = self.nums[-1], len(self.nums) - 1
        self.nums[last_index], self.index_map[last_num] = last_num, last_index
        self.nums.pop()
        del self.index_map[val]
        return True

    def getRandom(self) -> int:
        import random
        return random.choice(self.nums)