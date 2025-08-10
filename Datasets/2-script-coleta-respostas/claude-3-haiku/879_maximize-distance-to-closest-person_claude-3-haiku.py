class Solution:
    def maxDistToClosest(self, seats):
        pre_zeros, suf_zeros, max_zeros, zeros = -1, -1, -1, 0
        for i, seat in enumerate(seats):
            if seat == 0:
                zeros += 1
            else:
                if pre_zeros == -1:
                    pre_zeros = i
                suf_zeros = i
        max_zeros = max(pre_zeros, len(seats) - 1 - suf_zeros, (zeros + 1) // 2)
        return max_zeros