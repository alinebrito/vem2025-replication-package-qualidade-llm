class Solution(object):
    def customSortString(self, order, s):
        order_map = {char: i for i, char in enumerate(order)}
        return ''.join(sorted(s, key=lambda x: order_map.get(x, len(order))))