class Solution:
    def __init__(self):
        self.data = [None] * 1000001

    def put(self, key: int, value: int) -> None:
        self.data[key] = value

    def get(self, key: int) -> int:
        if self.data[key] is None:
            return -1  
        return self.data[key]

    def remove(self, key: int) -> None:
        self.data[key] = None  