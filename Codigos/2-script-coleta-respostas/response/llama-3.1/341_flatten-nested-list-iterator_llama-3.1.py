class Solution:
    def __init__(self, nestedList):
        self.stack = [[nestedList, 0]]

    def next(self):
        self.hasNext()
        nested, index = self.stack[-1]
        self.stack[-1][1] += 1
        return nested[index]

    def hasNext(self):
        while self.stack:
            nested, index = self.stack[-1]
            if index == len(nested):
                self.stack.pop()
            else:
                if isinstance(nested[index], list):
                    self.stack[-1][1] += 1
                    self.stack.append([nested[index], 0])
                else:
                    return True
        return False