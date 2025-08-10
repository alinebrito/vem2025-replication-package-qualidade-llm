class Solution:
    def __init__(self):
        self.data = [None] * 1000001

    def put(self, key: int, value: int) -> None:
        index = key % 1000001
        if self.data[index] is None:
            self.data[index] = [(key, value)]
        else:
            for i, (k, v) in enumerate(self.data[index]):
                if k == key:
                    self.data[index][i] = (key, value)
                    return
            self.data[index].append((key, value))

    def get(self, key: int) -> int:
        index = key % 1000001
        if self.data[index] is not None:
            for k, v in self.data[index]:
                if k == key:
                    return v
        return -1

    def remove(self, key: int) -> None:
        index = key % 1000001
        if self.data[index] is not None:
            for i, (k, v) in enumerate(self.data[index]):
                if k == key:
                    del self.data[index][i]
                    return