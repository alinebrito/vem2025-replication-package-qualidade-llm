class Solution:
    def __init__(self):
        self.dic = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dic:
            self.dic[key] = []
        self.dic[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dic:
            return ""
        values = self.dic[key]
        left, right = 0, len(values) - 1
        while left <= right:
            mid = (left + right) // 2
            if values[mid][0] <= timestamp:
                if mid == len(values) - 1 or values[mid + 1][0] > timestamp:
                    return values[mid][1]
                left = mid + 1
            else:
                right = mid - 1
        return ""