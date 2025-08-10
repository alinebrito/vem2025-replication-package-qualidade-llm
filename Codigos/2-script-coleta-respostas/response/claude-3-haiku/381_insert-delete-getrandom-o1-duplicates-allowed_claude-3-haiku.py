class Solution:
class RandomizedCollection:

    def __init__(self):
        self.nums = []
        self.indices = {}

    def insert(self, val: int) -> bool:
        self.indices.setdefault(val, set()).add(len(self.nums))
        self.nums.append(val)
        return len(self.indices[val]) == 1

    def remove(self, val: int) -> bool:
        if val not in self.indices:
            return False
        index = self.indices[val].pop()
        last_element = self.nums[-1]
        self.nums[index] = last_element
        self.indices[last_element].add(index)
        self.indices[last_element].discard(len(self.nums) - 1)
        self.nums.pop()
        if not self.indices[val]:
            del self.indices[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)