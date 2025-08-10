class Solution:
    def __init__(self, iterator):
        self.iter = iterator
        self.next_val = self.iter.next() if self.iter.hasNext() else None

    def next(self):
        ret = self.next_val
        self.next_val = self.iter.next() if self.iter.hasNext() else None
        return ret

    def hasNext(self):
        return self.next_val is not None

    def peek(self):
        return self.next_val