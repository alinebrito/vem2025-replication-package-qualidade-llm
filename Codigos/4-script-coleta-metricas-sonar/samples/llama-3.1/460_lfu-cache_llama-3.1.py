class Solution:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_count = {}
        self.count_node = defaultdict(OrderedDict)
        self.min_count = 0

    def get(self, key: int) -> int:
        if key not in self.key_count:
            return -1
        count = self.key_count[key]
        del self.count_node[count][key]
        if not self.count_node[count]:
            del self.count_node[count]
        self.key_count[key] = count + 1
        self.count_node[count + 1][key] = None
        self.min_count = min(self.count_node.keys())
        return self.key_count[key] - 1

    def put(self, key: int, value: int) -> None:
        if not self.capacity:
 return if key in self.key_count:
            self.key_count[key] += 1
            del self.count_node[self.key_count[key] - 1][key]
            self.count_node[self.key_count[key]][key] = None
            self.min_count = min(self.count_node.keys())
        else:
            if len(self.key_count) == self.capacity:
                k, _ = self.count_node[self.min_count].popitem(last=False)
                del self.key_count[k]
            self.key_count[key] =1
            self.count_node[1][key] = None
            self.min_count = 1