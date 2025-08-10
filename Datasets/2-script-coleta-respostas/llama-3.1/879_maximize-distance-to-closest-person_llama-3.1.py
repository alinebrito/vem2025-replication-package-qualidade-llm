class Solution:
    def maxDistToClosest(self, seats):
        pre_zeros, suf_zeros, max_zeros, zeros = -1, -1, -1, 0
        for i, seat in enumerate(seats):
            if seat == 1:
                if pre_zeros == -1:
                    pre_zeros = i
                else:
                    max_zeros = max(max_zeros, i - pre_zeros -1)
                    zeros = i - pre_zeros -1
                    pre_zeros = i
            else:
                zeros +=1
        suf_zeros = len(seats) -1 - pre_zeros -1 if pre_zeros != -1 else len(seats)-1
        return max(max_zeros //2 + (max_zeros % 2), pre_zeros, suf_zeros)
