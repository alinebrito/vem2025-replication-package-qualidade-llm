class Solution:
    def __init__(self, nestedList):
        self.stack = [[nestedList, 0]]

    def next(self):
        self.hasNext()
        nested, index = self.stack[-1]
        value = nested[index]
        self.stack[-1][1] += 1
        return value

    def hasNext(self):
        while self.stack:
            nested, index = self.stack[-1]
            if index == len(nested):
                self.stack.pop()
                continue
            value = nested[index]
            if isinstance(value, list):
                self.stack[-1][1] += 1
                self.stack.append([value, 0])
            else:
                return True
        return False