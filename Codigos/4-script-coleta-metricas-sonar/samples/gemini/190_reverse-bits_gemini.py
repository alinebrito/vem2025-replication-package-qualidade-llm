class Solution:
    def reverseBits(self, n):
        oribin='{0:032b}'.format(n)
        return int(oribin[::-1],2)