class Solution:
    def __init__(self):
        self.vals = []
        self.val_map = {}
    
    def insert(self, val: int) -> bool:
        if val not in self.val_map:
            self.val_map[val] = set()
        self.val_map[val].add(len(self.vals))
        self.vals.append(val)
        return len(self.val_map[val]) == 1
    
    def remove(self, val: int) -> bool:
        if val not in self.val_map or not self.val_map[val]:
            return False  
        idx_to_remove = self.val_map[val].pop()
        last_val = self.vals[-1]
        self.vals[idx_to_remove] = last_val  
        if self.val_map[last_val]:
            self.val_map[last_val].remove(len(self.vals) - 1)
            self.val_map[last_val].add(idx_to_remove)
        self.vals.pop()
        if not self.val_map[val]:
            del self.val_map[val]
        return True
    
    def getRandom(self) -> int:
        import random  
        return random.choice(self.vals)