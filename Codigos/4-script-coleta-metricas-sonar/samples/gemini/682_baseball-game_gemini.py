class Solution:
    def calPoints(self, ops):
        p = []
        for x in ops:
            if x == '+':
                p.append(p[-1] + p[-2])
            elif x == 'D':
                p.append(p[-1] * 2)
            elif x == 'C':
                p.pop()
            else:
                p.append(int(x))
        return sum(p)