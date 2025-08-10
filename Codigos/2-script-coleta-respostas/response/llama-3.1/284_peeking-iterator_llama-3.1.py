class Solution:
    def __init__(self, iterator):
        self.iter = iterator
        self.temp = None

    def next(self):
        if self.temp is not None:
            temp = self.temp
            self.temp = None
            return temp
        return next(self.iter)

    def hasNext(self):
        if self.temp is not None:
            return True
        try:
            self.temp = next(self.iter)
        except StopIteration:
            return False
        return True

    def peek(self):
        if self.temp is not None:
            return self.temp
        self.temp = next(self.iter)
        return self.temp