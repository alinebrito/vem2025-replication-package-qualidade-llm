class Solution:
    def without_stack(self, S):
        opening = count = 0
        for i in S:
            if i == '(':
                opening += 1
            else:
                opening -= 1
            if opening < 0:
                count += 1
                opening += 1
        return count + opening