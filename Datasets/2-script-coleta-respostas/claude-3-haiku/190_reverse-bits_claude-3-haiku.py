class Solution:
    def reverseBits(self, n):
        oribin = '{0:032b}'.format(n)
        revbin = oribin[::-1]
        return int(revbin, 2)