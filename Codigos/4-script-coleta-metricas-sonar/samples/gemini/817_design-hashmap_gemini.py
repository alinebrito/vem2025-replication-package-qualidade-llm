class Solution:
    def __init__(self):
        self.data = [None] * 1000001

    def put(self, key, value):
        self.data[key] = value

    def get(self, key):
        if self.data[key] is not None:
            return self.data[key]
        else:
            return -1

    def remove(self, key):
        self.data[key] = None