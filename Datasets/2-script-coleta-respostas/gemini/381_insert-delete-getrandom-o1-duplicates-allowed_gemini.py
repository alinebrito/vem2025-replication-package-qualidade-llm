class Solution:
    def __init__(self):
        self.nums = []
        self.idx = {}

    def insert(self, val):
        self.idx.setdefault(val, set()).add(len(self.nums))
        self.nums.append(val)
        return len(self.idx[val]) == 1

    def remove(self, val):
        if val not in self.idx:
            return False
        i = self.idx[val].pop()
        last = self.nums[-1]
        if i != len(self.nums) - 1:
            self.nums[i] = last
            self.idx[last].remove(len(self.nums) - 1)
            self.idx[last].add(i)
        self.nums.pop()
        return True

    def getRandom(self):
        return self.nums[random.randint(0, len(self.nums) - 1)]