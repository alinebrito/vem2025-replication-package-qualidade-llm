class Solution:
    def __init__(self, iterator):
        self.iter = iterator
        self.next_val = None
        self.has_next = False

    def next(self):
        if self.has_next:
            val = self.next_val
            self.has_next = False
            return val
        else:
            return self.iter.next()

    def hasNext(self):
        if self.has_next:
            return True
        self.next_val = self.iter.next()
        self.has_next = True
        return True

    def peek(self):
        if self.has_next:
            return self.next_val
        else:
            self.next_val = self.iter.next()
            self.has_next = True
            return self.next_val