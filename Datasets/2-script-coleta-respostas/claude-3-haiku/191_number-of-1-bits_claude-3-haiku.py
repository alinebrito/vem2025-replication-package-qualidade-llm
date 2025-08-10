class Solution:
    def using_inbuilt_counter(self, n):
        counter = collections.Counter(bin(n)[2:])
        return counter['1']