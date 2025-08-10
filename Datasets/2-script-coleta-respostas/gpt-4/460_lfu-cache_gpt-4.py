class Solution:
    class LFUCache:
        def __init__(self, capacity: int):
            self.capacity = capacity
            self.min_freq = 0
            self.key_value = {}
            self.key_freq = {}
            self.freq_keys = defaultdict(OrderedDict)

        def _update(self, key: int):
            freq = self.key_freq[key]
            del self.freq_keys[freq][key]
            if not self.freq_keys[freq]:
                del self.freq_keys[freq]
                if self.min_freq == freq:
                    self.min_freq += 1
            self.key_freq[key] += 1
            self.freq_keys[self.key_freq[key]][key] = None

        def get(self, key: int) -> int:
            if key not in self.key_value:
                return -1
            self._update(key)
            return self.key_value[key]

        def put(self, key: int, value: int) -> None:
            if self.capacity <= 0:
                return
            if key in self.key_value:
                self.key_value[key] = value
                self._update(key)
            else:
                if len(self.key_value) >= self.capacity:
                    lfu_key, _ = self.freq_keys[self.min_freq].popitem(last=False)
                    del self.key_value[lfu_key]
                    del self.key_freq[lfu_key]
                self.key_value[key] = value
                self.key_freq[key] = 1
                self.freq_keys[1][key] = None
                self.min_freq = 1