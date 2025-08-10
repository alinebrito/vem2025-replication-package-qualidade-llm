class Solution:
    def without_stack(self, S):
        opening = count = 0
        for c in S:
            if c == '(':
                opening += 1
            else:
                if opening > 0:
                    opening -= 1
                else:
                    count += 1
        return count + opening