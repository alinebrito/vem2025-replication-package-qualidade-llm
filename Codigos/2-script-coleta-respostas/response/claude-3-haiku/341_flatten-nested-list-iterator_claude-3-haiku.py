class Solution:
    def __init__(self, nestedList):
        self.stack = [[nestedList, 0]]

    def hasNext(self):
        while self.stack:
            nested_list, index = self.stack[-1]
            if index < len(nested_list):
                item = nested_list[index]
                self.stack[-1][1] += 1
                if isinstance(item, list):
                    self.stack.append([item, 0])
                else:
                    return True
            else:
                self.stack.pop()
        return False

    def next(self):
        return self.stack[-1][0][self.stack[-1][1] - 1]