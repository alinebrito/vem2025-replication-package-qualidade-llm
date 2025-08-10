class Solution:
    def __init__(self):
        self.mp = {}

    def add(self, key: int) -> None:
        self.mp[key] = 1

    def remove(self, key: int) -> None:
        if key in self.mp:
            del self.mp[key]

    def contains(self, key: int) -> bool:
        return key in self.mp