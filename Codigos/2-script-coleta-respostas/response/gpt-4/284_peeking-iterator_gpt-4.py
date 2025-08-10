class Solution:
    class PeekingIterator:
        def __init__(self, iterator):
            self.iterator = iterator  
            self._next = None  
            self._has_next = None  
            if self.iterator.hasNext():
                self._next = self.iterator.next()
                self._has_next = True  
            else:
                self._has_next = False

        def peek(self):
            return self._next

        def next(self):
            current = self._next  
            self._has_next = self.iterator.hasNext()
            if self._has_next:
                self._next = self.iterator.next()
            else:
                self._next = None  
            return current

        def hasNext(self):
            return self._has_next  