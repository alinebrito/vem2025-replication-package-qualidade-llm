class Solution:
class TimeMap:

    def __init__(self):
        self.dic = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dic:
            self.dic[key] = []
        self.dic[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dic:
            return ""
        l, r = 0, len(self.dic[key]) - 1
        while l <= r:
            mid = (l + r) // 2
            if self.dic[key][mid][0] <= timestamp:
                l = mid + 1
            else:
                r = mid - 1
        return self.dic[key][r][1] if r >= 0 else ""