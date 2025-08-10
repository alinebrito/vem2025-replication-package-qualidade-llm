class Solution(object):
    def customSortString(self, order, s):
        order_dict = {char: i for i, char in enumerate(order)}
        sorted_s = sorted(s, key=lambda x: order_dict[x])
        return ''.join(sorted_s)