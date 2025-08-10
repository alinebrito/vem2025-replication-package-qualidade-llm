class Solution:
    def __init__(self):
        self.size = 1009
        self.table = [[] for _ in range(self.size)]

    def _hash(self, key):
        return key % self.size

    def add(self, key):
        h = self._hash(key)
        if key not in self.table[h]:
            self.table[h].append(key)

    def contains(self, key):
        h = self._hash(key)
        return key in self.table[h]

    def remove(self, key):
        h = self._hash(key)
        if key in self.table[h]:
            self.table[h].remove(key)