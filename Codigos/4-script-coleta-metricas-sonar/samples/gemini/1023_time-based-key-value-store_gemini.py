class Solution:
    def __init__(self):
        self.dic = {}

    def set(self, key, value, timestamp):
        if key not in self.dic:
            self.dic[key] = []
        self.dic[key].append([timestamp, value])

    def get(self, key, timestamp):
        if key not in self.dic:
            return ""
        values = self.dic[key]
        l, r = 0, len(values) - 1
        while l <= r:
            mid = (l + r) // 2
            if values[mid][0] <= timestamp:
                l = mid + 1
            else:
                r = mid - 1
        return "" if r == -1 else values[r][1]