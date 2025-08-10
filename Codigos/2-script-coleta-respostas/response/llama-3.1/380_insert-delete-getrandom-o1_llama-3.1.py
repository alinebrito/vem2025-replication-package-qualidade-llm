class Solution:
    def __init__(self):
        self.data_map = {}
        self.data_list = []

    def insert(self, val: int) -> bool:
        if val not in self.data_map:
            self.data_map[val] = len(self.data_list)
            self.data_list.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.data_map:
            last, idx = self.data_list[-1], self.data_map[val]
            self.data_list[idx], self.data_map[last] = last, idx
            self.data_list.pop()
            del self.data_map[val]
            return True
        return False

 def getRandom(self) -> int:
        return random.choice(self.data_list)