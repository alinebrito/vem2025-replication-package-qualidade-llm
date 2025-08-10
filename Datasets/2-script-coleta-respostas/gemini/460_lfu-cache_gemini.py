class Solution:
from collections import deque, defaultdict, OrderedDict

class Solution:
    class LFUCache:
        def __init__(self, capacity):
            self.capacity = capacity
            self.key_to_value = {}
            self.key_to_freq = {}
            self.freq_to_keys = defaultdict(OrderedDict)
            self.min_freq = 0

        def get(self, key):
            if key not in self.key_to_value:
                return -1
            
            self.update_freq(key)
            return self.key_to_value[key]

        def put(self, key, value):
            if self.capacity == 0:
                return

            if key in self.key_to_value:
                self.key_to_value[key] = value
                self.update_freq(key)
                return
            
            if len(self.key_to_value) == self.capacity:
                self.remove_lfu_key()
            
            self.key_to_value[key] = value
            self.key_to_freq[key] = 1
            self.freq_to_keys[1][key] = None
            self.min_freq = 1

        def update_freq(self, key):
            old_freq = self.key_to_freq[key]
            new_freq = old_freq + 1
            self.key_to_freq[key] = new_freq

            del self.freq_to_keys[old_freq][key]
            self.freq_to_keys[new_freq][key] = None

            if not self.freq_to_keys[old_freq]:
                del self.freq_to_keys[old_freq]
                if old_freq == self.min_freq:
                    self.min_freq = new_freq

        def remove_lfu_key(self):
            lfu_key, _ = self.freq_to_keys[self.min_freq].popitem(last=False)
            del self.key_to_value[lfu_key]
            del self.key_to_freq[lfu_key]
            if not self.freq_to_keys[self.min_freq]:
                del self.freq_to_keys[self.min_freq]