class Solution:
    def maxDistToClosest(self, seats):
        pre_zeros, suf_zeros, max_zeros, zeros = -1, -1, -1, 0
        n = len(seats)
        for i in range(n):
            if seats[i] == 0:
                zeros += 1
            else:
                if pre_zeros == -1:
                    max_zeros = zeros
                else:
                    max_zeros = max(max_zeros, (zeros + 1) // 2)
                pre_zeros = zeros
                zeros = 0
        max_zeros = max(max_zeros, zeros)
        return max(max_zeros, pre_zeros + zeros)