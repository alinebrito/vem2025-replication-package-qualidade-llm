class Solution:
    def reconstructQueue(self, people):
        result = []
        for p in people:
            result.insert(p[1], p)
        return result