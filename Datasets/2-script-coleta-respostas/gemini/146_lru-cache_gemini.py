class Solution:
  def __init__(self, capacity):
    self.capacity = capacity
    self.cache = {}
    # Use OrderedDict to maintain insertion order for LRU
    self.order = collections.OrderedDict()

  def get(self, key):
    if key not in self.cache:
      return -1
    # Move accessed key to the front of the order
    self.order.move_to_end(key)
    return self.cache[key]

  def put(self, key, value):
    if key in self.cache:
      self.order.move_to_end(key)
    else:
      if len(self.cache) == self.capacity:
        # Remove least recently used item (first in OrderedDict)
        del self.cache[self.order.popitem(last=False)[0]]
      self.order[key] = None  # Mark as most recently used
    self.cache[key] = value