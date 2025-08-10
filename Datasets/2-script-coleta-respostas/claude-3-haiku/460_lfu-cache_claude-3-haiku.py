class Solution:
class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.freq = defaultdict(int)
        self.order = OrderedDict()
        self.least_freq = 1

    def get(self, key: int) -> int:
        if key not in self.order:
            return -1
        self.freq[key] += 1
        self.order.move_to_end(key)
        if self.least_freq == self.freq[self.order.popitem(last=False)[0]]:
            self.least_freq += 1
        return self.order[key]

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key in self.order:
            self.freq[key] += 1
            self.order.move_to_end(key)
        else:
            if len(self.order) == self.capacity:
                lfu_key, _ = self.order.popitem(last=False)
                del self.freq[lfu_key]
                if self.least_freq == self.freq[lfu_key]:
                    self.least_freq += 1
            self.order[key] = value
            self.freq[key] = 1
            self.least_freq = 1