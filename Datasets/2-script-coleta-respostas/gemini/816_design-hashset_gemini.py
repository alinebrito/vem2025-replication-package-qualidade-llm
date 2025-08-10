class Solution:
    def __init__(self):
        self.size = 1000
        self.table = [None] * self.size
        

    def add(self, key):
        index = self._hash(key)
        if self.table[index] is None:
            self.table[index] = [key]
        else:
            self.table[index].append(key)
        

    def contains(self, key):
        index = self._hash(key)
        if self.table[index] is not None:
            for k in self.table[index]:
                if k == key:
                    return True
        return False
        

    def remove(self, key):
        index = self._hash(key)
        if self.table[index] is not None:
            original_size = len(self.table[index])
            self.table[index] = [k for k in self.table[index] if k != key]
            if len(self.table[index]) < original_size:
                return
        

    def _hash(self, key):
        return key % self.size